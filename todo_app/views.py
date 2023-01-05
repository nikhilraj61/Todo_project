from django.shortcuts import render,redirect
from . models import *
# from . models import task
from . forms import todoforms
#todoforms mean's' form's table name#
# Create your views here.


def home(request):
    obj1=task.objects.all()
    if request.method =='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        priority=request.POST.get('priority')
        email=request.POST.get('email')
        date=request.POST.get('date')
        obj=task(name =name,age=age,priority=priority,email=email,date=date)
        obj.save()
        return redirect('/')
    return render(request,'home.html',{'obj1':obj1})
#
def delete(request,taskid):
    ta=task.objects.get(id=taskid)
    if request.method == 'POST':
        ta.delete()
        return redirect('/')
    return render(request,'delete.html',{'ta':ta})

#
def update(request,id):
    av=task.objects.get(id=id)
    form=todoforms(request.POST or None,instance=task)  #instance keyword argument is passed the model whose relations that the formset will edit
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'av':av,'form':form})