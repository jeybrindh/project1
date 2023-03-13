from django.shortcuts import render
from django.shortcuts import render, redirect  
from crud.forms import EmployeeForm  
from crud.models import * 
 
def upload(request):  
    if request.method == "POST":  
       form = EmployeeForm(request.POST)  
       if form.is_valid():  
            try:  
               form.save()  
                
               return redirect('index.html')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'login.html')
    # {'form':form}
def index(request):
    return render(request,'index.html')