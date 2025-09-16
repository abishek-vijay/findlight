from django.shortcuts import render
from friendlist.models import Friendlist

# Create your views here.




def viewfriend(request):
    ss=request.session["u_id"]
    ob = Friendlist.objects.filter(us_id=ss)
    context = {
        'objfrd': ob
    }
    return render(request,'friendlist/view friend.html',context)


def approve(request,idd):
    ob=Friendlist.objects.get(f_id=idd)
    ob.status='accepted'
    ob.save()
    return viewfriend(request)

def reject(request,idd):
    ob=Friendlist.objects.get(f_id=idd)
    ob.status='rejected'
    ob.save()
    return viewfriend(request)

