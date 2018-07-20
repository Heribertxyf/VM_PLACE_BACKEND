"""vm_place_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^client/', views.ClientAPI.as_view()),
    url(r'^history_place?$', views.HistoryPlaceAPI.as_view()),
    url(r'^client_vms_place?$', views.ClientVMAPI.as_view()),
    url(r'^update_host_status?$', views.UpdateHostStatusAPI.as_view()),
    url(r'^update_vm_place?$', views.UpdateVMPlaceAPI.as_view()),
]
