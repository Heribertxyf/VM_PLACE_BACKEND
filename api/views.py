# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from serializers import ClientSerializer, HistoryPlaceSerializer, ClientVMSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from db.cmdb import Client, HistoryPlace, VM, VC, Host
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
# Create your views here.



class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "size"
    max_page_size =200
    page_query_param = "page"


class ClientAPI(APIView):
    def post(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class HistoryPlaceAPI(APIView):
    def post(self, request, format=None):
        vm_place = {}
        status = False
        msg = ""
        vm_name = request.POST.get('vm_name')
        if vm_name:
            if HistoryPlace.objects.filter(vm__name=vm_name).count() > 0:
                history_place = HistoryPlace.objects.get(vm__name=vm_name)
                serializer = HistoryPlaceSerializer(history_place)
                status = True
                vm_place = serializer.data
            else:
                msg = "没有找到VM"
        else:
            msg = "输入为空，请重新输入"
        return Response({"status": status, "msg": msg, "vm_name": vm_name, "vm_place": vm_place})


class ClientVMAPI(APIView):
    def post(self, request, *args, **kwargs):
        data = []
        status = False
        msg = ""
        page = request.GET.get('page',1)
        size = request.GET.get('size',1)
        search = request.GET.get('search', None)
        client_name = request.POST.get('client_name')
        if client_name:
            if search:
                search_filter = Q(vm__client__name=client_name) & (Q(vm__name__contains=search) | Q(place1__name__contains=search))
            else:
                search_filter = Q(vm__client__name=client_name)
            vms_place = HistoryPlace.objects.filter(search_filter).order_by('created_at').reverse()
            if vms_place.count() > 0:
                pg = MyPageNumberPagination()
                vm_place = pg.paginate_queryset(queryset=vms_place, request=request, view=self)
                ser = ClientVMSerializer(instance=vm_place, many=True)
                for vm_info in ser.data:
                    data.append([vm_info['vm'], vm_info['place']])
                status = True
            else:
                msg = "未找到客户云主机"
        else:
            msg = "输入为空，请重新输入"
        return Response({"status": status, "msg": msg, "client": client_name, "data": data, "total": len(data), "size": size, "page": page})



