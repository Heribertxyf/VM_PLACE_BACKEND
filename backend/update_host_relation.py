# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from db.models import *
from django.db.models import Q
import re
import ssl
import atexit
import traceback
import logging
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
# ssl context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE


def connect_vc(host, username, password):
    """
        登录 vc 或者esxi宿主机
    :param host: vCenter或ESXI Server地址
    :param username: vCenter或ESXI用户名
    :param password:
    :return: vCenter or ESXI Content
    """
    try:
        si = SmartConnect(
            host=host,
            user=username,
            pwd=password,
            port=443,
            sslContext=context)
        return si
    except vim.fault.InvalidLogin:
        print (u'由于用户名或密码不正确，无法完成登录。')
    except Exception:
        print (traceback.format_exc())


def disconnect_vc(si):
    """
        断开连接
    :param si:
    :return:
    """
    Disconnect(si)


def get_vc_dc(vc_content):
    """
        获取指定content的数据中心
    :param vc_content: vCenter content
    :return: datacenter object
    """
    root_folder = vc_content.rootFolder
    dc_list = [dc for dc in root_folder.childEntity
               if isinstance(dc, vim.Datacenter)]
    return dc_list


def get_dc_clusters(datacenter):
    clusters = []
    host_folder = datacenter.hostFolder
    for cluster in host_folder.childEntity:
        if hasattr(cluster, 'host'):
            clusters.append(cluster)
    return clusters


def get_host_ip(host_obj):
    """
        通过 host obj 获取 ip
    :param host_obj:
    :return:
    """
    host_vnics = host_obj.config.network.vnic
    for vnic in host_vnics:
        device = vnic.device
        if device == 'vmk0':
            ip_address = vnic.spec.ip.ipAddress
            return ip_address


def init_vc_info(vc):
    si = connect_vc(host=vc.ip, username=vc.username, password=vc.password)
    datacenters = get_vc_dc(si.content)
    datacenters_name = []
    clusters_name = []
    hosts = []
    error_hosts = []
    hosts_ip = {}
    for datacenter in datacenters:
        pod_obj = Pod.objects.create(name=datacenter.name, vc=vc)
        clusters = get_dc_clusters(datacenter)
        for cluster in clusters:
            cluster_obj = Cluster.objects.create(name=cluster.name, pod=pod_obj)
            for host in cluster.host:
                try:
                    host_name = re.search("(pod\d*-clu\d*-h\d*)", host.name).group()
                    host_ip = get_host_ip(host_obj=host)
                    Host.objects.create(name=host_name, ip=host_ip, cluster=cluster_obj)
                except Exception:
                    error_hosts.append(host.name)
                    # 当host主机故障的时候，调过故障主机
                    continue
    disconnect_vc(si)
    return


def verify_vc(name, ip):
    search_filter = Q(name=name) | Q(ip=ip)
    if VC.objects.filter(search_filter).count() > 0:
        return False
    else:
        return True


def verify_site(name, display):
    search_filter = Q(name=name) | Q(display_name=display)
    if Site.objects.filter(search_filter).count() > 0:
        return False
    else:
        return True




