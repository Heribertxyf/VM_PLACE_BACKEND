from rest_framework import serializers
from db.cmdb import Client, Site, Pod, Cluster, VC, VM, Host, HistoryPlace
import json


class ClientSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Client
        fields = ('id','uuid','name','email','phone','created_at')


class HistoryPlaceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    place1 = serializers.SerializerMethodField()
    place2 = serializers.SerializerMethodField()
    place3 = serializers.SerializerMethodField()
    place4 = serializers.SerializerMethodField()
    place5 = serializers.SerializerMethodField()

    class Meta:
        model = HistoryPlace
        fields = ('place1','place2','place3','place4','place5','created_at')
    def get_place1(self, obj):
        if obj.place1:
            return obj.place1.name
        else:
            return None
    def get_place2(self, obj):
        if obj.place2:
            return obj.place2.name
        else:
            return None
    def get_place3(self, obj):
        if obj.place3:
            return obj.place3.name
        else:
            return None
    def get_place4(self, obj):
        if obj.place4:
            return obj.place4.name
        else:
            return None
    def get_place5(self, obj):
        if obj.place5:
            return obj.place5.name
        else:
            return None

class ClientVMSerializer(serializers.ModelSerializer):
    vm = serializers.SerializerMethodField()
    place = serializers.SerializerMethodField()
    class Meta:
        model = HistoryPlace
        fields = ('vm', 'place')
    def get_vm(self, obj):
        return obj.vm.name
    def get_place(self, obj):
        if obj.place1:
            return obj.place1.name
        else:
            return None