from django.shortcuts import render,HttpResponse
from matplotlib.style import context
from requests import request
from datetime import datetime
from Myapp.models import Contact
def index(responce):
    return render(responce,'index.html')
# Create your views here.
def about(responce):
     return render(responce,'about.html')
    

def services(responce):
     return render(responce,'services.html')
    
    
def contactus(request):
     if request.method =="post":
          name = request.post.GET('name')
          email = request.post.GET('email')
          phone = request.post.GET('phone')
          desc = request.post.GET('desc')
          
          contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
          contact.save()
     
     return render(request,'contact.html')
    # return HttpResponse('hello this is contact page')
