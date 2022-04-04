
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from.forms import StudentRegistration
from.models import User
# Create your views here.
# This function will add new item
def add_show(request):
    print("hello")
    if request.method =='POST':
        fm= StudentRegistration(request.POST,request.FILES)
        print(request.FILES ,"hello")
        if fm.is_valid():
            # nm=fm.cleaned_data['name']
            # em=fm.cleaned_data['email']
            # pm=fm.cleaned_data['number']   
            # print(nm)
            # print(em)
            # print(pm)
            
            # reg= User(name=nm,email=em,number=pm)
            # reg.save() 
            fm.save()
            fm= StudentRegistration()
       
    else:
        fm =StudentRegistration()  
    stud =User.objects.all()     
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

# this function update and edit 
def update_data(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)    
        fm=StudentRegistration(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()    
    else:
        pi=User.objects.get(pk=id)    
        fm=StudentRegistration(instance=pi)      
    return render(request,'enroll/updatestudent.html',{'form':fm})
#this function will delete
def delete_data(request,id):
    if request.method=="POST":
        pi =User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
