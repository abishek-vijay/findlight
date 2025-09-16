from django.shortcuts import render
from counsellor.models import Counsellor
from chat.models import Chat
import datetime
from django.db.models import Q
from user.models import User
# Create your views here.
from login.models import Login


def con(request):
    ob= Counsellor.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/viewcon.html',context)

def cochat(request,idd):
    ss=request.session ["u_id"]
    obj = Counsellor.objects.get(c_id=idd)
    ob = Chat.objects.filter(Q(us_id=ss) & Q(c_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.c_id=idd
        obk.us_id=ss
        obk.date = datetime.date.today()
        obk.time = datetime.datetime.now()
        obk.rectype="consellor"
        obk.sendertype = "user"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)



def std(request):
    ob= User.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)


def stchat(request,idd):
    ss = request.session ["u_id"]
    obj = User.objects.get(us_id=idd)
    ob=Chat.objects.filter(Q(us_id=idd) & Q(c_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=Chat()
        obk.message=request.POST.get('mssg')
        obk.us_id=idd
        obk.c_id=ss
        obk.date=datetime.date.today()
        obk.time=datetime.datetime.now()
        obk.rectype="user"
        obk.sendertype="consellor"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
