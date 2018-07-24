# -*- coding: utf-8 -*-
from views import *


class CreateVC(APIView):
    def post(self, request, format=None):
        name = request.POST.get("name")
        ip = request.POST.get("ip")
        port = request.POST.get("port")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if verify_vc(name, ip):
            vc = VC.objects.create(name=name, ip=ip, port=port, username=username, password=password)
            init_vc_info(vc)
            data = {"status": True, "msg": "VC创建，初始化成功"}
        else:
            data = {"status": False, "msg": "VC创建失败"}
        return Response(data)


class CreateSite(APIView):
    def post(self, request, format=None):
        name = request.POST.get("name")
        display = request.POST.get("display_name")
        if verify_site():
            Site.objects.create(name=name, display_name=display)
            data = {"status": True, "msg": "Site创建成功"}
        else:
            data = {"status": False, "msg": "Site创建失败"}
        return Response(data)


class RelateSitePod(APIView):
    def post(self, request, format=None):
        site_id = request.POST.get("site_id")
        pod_id = request.POST.get("pod_id")
        site = Site.objects.get(id=site_id)
        pod = Pod.objects.get(id=pod_id)
        pod.site = site
        pod.save()
        return Response({"status": True, "msg": "操作成功"})



