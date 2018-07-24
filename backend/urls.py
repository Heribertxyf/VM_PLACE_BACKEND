from django.conf.urls import url

from update_host_relation import *


urlpatterns = [
    url(r'create_site', create_site()),
]