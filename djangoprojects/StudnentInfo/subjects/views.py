from django.shortcuts import render,redirect
from subjects.models import studentinfo
# Create your views here.
from subjects.forms import StudentForm

def home(request):
    return httpRequest('Hi there amey here')

def info(request):
    students=studentinfo.objects.all()
    return render(request,'subjects/info.html',{'students':students})

def createstud(request):
    stud=StudentForm()
    if request.method=='POST':
        stud=StudentForm(request.POST)
        if stud.is_valid():
            stud.save()
        return redirect('/info')

    return render(request,'subjects/createstud.html',{'stud':stud})

def delete(request,id):
    stud=studentinfo.objects.get(id=id)
    stud.delete()
    return redirect('/info')

def update(request,Name):
    stud=studentinfo.objects.get(Name=Name)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
        return redirect('/info')
    return render(request,'subjects/update.html',{'stud':stud})
