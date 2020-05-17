from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Entery

def delete(request):
    id =request.GET['id']
    Entery.objects.filter(id=id).delete()
    return HttpResponseRedirect("show")

def home(request):
    return render(request,"home.html")

def show(request):
    data =Entery.objects.all()
    return render(request,"show.html",{'data':data})

def send(request):
    if request.method=='POST':
        id=request.POST['id']
        data1=request.POST['data1']
        data2=request.POST['data2']
        Entery(id=id,data1=data1,data2=data2).save()
        msg="record stored successfilly"
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse('404')


def edit(request):
    id=request.GET['id']
    data1=data2="not_available"
    for data in Entery.objects.filter(id=id):
        data1=data.data1
        data2=data.data2

    return render(request,"edit.html",{'id':id,'data1':data1,'data2':data2})


def recordedit(request):
    if request.method=='POST':
        id=request.POST['id']
        data1=request.POST['data1']
        data2=request.POST['data2']
        Entery.objects.filter(id=id).update(data1=data1,data2=data2)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse('404')
# Create your views here.
