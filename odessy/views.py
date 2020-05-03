from django.shortcuts import render
from odessy.models import ody
from odessy.models import hell
from odessy.models import od
from . import forms


 

def huu(request):
    form = forms.student()    
    if request.method == 'POST':
        form  = forms.yep(request.POST)
        if form.is_valid():
            print('form validation success and printing data')
            print('name',form.cleaned_data['en1'])
            print('name',form.cleaned_data['en2'])
            print('name',form.cleaned_data['en3'])
            print('name',form.cleaned_data['en4'])
            print('name',form.cleaned_data['en5'])
            print('name',form.cleaned_data['en6'])
            print('name',form.cleaned_data['en7'])
            print('name',form.cleaned_data['en9'])
            print('name',form.cleaned_data['en10'])    
    return render(request , 'index.html',{'form':form})
def  o(request):
    hi = od.objects.all()
     
    my_dict = {'hi':hi}
    return render(request,'base.html',context=my_dict)    
   
def syed(request):
 
    form = forms.ll
    if request.method == 'POST':
        form = forms.ll(request.POST)
        if form.is_valid():
            form.save(commit = True)
         
        return render(request,'base.html')    

    return render(request,'index.html',{'form' : form})


def sol(request):
    emp_list =  od.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'hello.html',context=my_dict)

def  o(request):
    hi = od.objects.all()
     
    my_dict = {'hi':hi}
    return render(request,'base.html',context=my_dict)    


 




