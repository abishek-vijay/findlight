from django.conf.urls import url
from chat import views

urlpatterns=[
    url('vc/',views.con),
    url('con/(?P<idd>\w+)',views.cochat),

    url('sc/',views.std),
    url('std/(?P<idd>\w+)',views.stchat),

]