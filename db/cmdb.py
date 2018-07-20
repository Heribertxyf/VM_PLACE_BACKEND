# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime


class Client(models.Model):
    uuid = models.CharField(max_length=255,default='',unique=True,null=False)
    name = models.CharField(max_length=255,default='',unique=False,null=False)
    email = models.CharField(max_length=255,default='',null=True,blank=True)
    phone = models.CharField(max_length=255,default='',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'client'
        verbose_name = 'client'


class Site(models.Model):
    name = models.CharField(max_length=255,default='',unique=False,null=False)
    display_name = models.CharField(max_length=255,default='',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'site'
        verbose_name = 'site'


class VC(models.Model):
    name = models.CharField(max_length=255,default='',unique=False,null=False)
    ip = models.CharField(max_length=255,default='',null=True,blank=True)
    port = models.IntegerField(default=443,null=True,blank=True)
    username = models.CharField(max_length=255,default='ops.user01',null=True,blank=True)
    password = models.CharField(max_length=255,default='cds-P@$$w0rd@2017',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'vc'
        verbose_name = 'vc'


class Pod(models.Model):
    name = models.CharField(max_length=255,default='',unique=False,null=False)
    site = models.ForeignKey(Site,default='',null=True)
    vc = models.ForeignKey(VC,default='',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'pod'
        verbose_name = 'pod'


class Cluster(models.Model):
    name = models.CharField(max_length=255,default='',unique=False,null=False)
    pod = models.ForeignKey(Pod,default='',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'cluster'
        verbose_name = 'cluster'


class Host(models.Model):
    name = models.CharField(max_length=255,default='',unique=False,null=False)
    ip = models.CharField(max_length=255,default='',unique=False,null=False)
    cluster = models.ForeignKey(Cluster,default='',null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'host'
        verbose_name = 'host'



class VM(models.Model):
    name = models.CharField(max_length=255,default='',unique=False,null=False)
    client = models.ForeignKey(Client,default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'vm'
        verbose_name = 'vm'

    @classmethod
    def create(cls, client_name, name):
        client = Client.objects.get(name=client_name)
        vm = VM.objects.create(name=name, client=client)
        return True, vm


class HistoryPlace(models.Model):
    vm = models.ForeignKey(VM,default='',unique=False,null=False)
    place1 = models.ForeignKey(Host,default='',null=True,related_name='place_current')
    place2 = models.ForeignKey(Host,default='',null=True,related_name='place_last_1')
    place3 = models.ForeignKey(Host,default='',null=True,related_name='place_last_2')
    place4 = models.ForeignKey(Host,default='',null=True,related_name='place_last_3')
    place5 = models.ForeignKey(Host,default='',null=True,related_name='place_last_4')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'history_place'
        verbose_name = 'history_place'

    @classmethod
    def update(cls, vm, place):
        if HistoryPlace.objects.filter(vm=vm).first():
            history = HistoryPlace.objects.get(vm=vm)
            if place.id != history.place1.id:
                history_place = [place, history.place1, history.place2, history.place3, history.place4]
                history.place1 = history_place[0]
                history.place2 = history_place[1]
                history.place3 = history_place[2]
                history.place4 = history_place[3]
                history.place5 = history_place[4]
                history.save()
        else:
            history = HistoryPlace.objects.create(vm=vm, place1=place)
        return True, history




