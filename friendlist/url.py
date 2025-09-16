from django.conf.urls import url
from friendlist import views

urlpatterns=[
    url('viewfriend/',views.viewfriend),
    url('accept/(?P<idd>\w+)',views.approve,name="accept"),
    url('reject/(?P<idd>\w+)',views.reject,name="reject")
]