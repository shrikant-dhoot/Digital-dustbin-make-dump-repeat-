from django.http import HttpResponse,JsonResponse
from django.shortcuts import render , redirect
from.models import * 
from.utils import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
     
     if request.method == "POST" :
          username = request.POST.get("username")
          email = request.POST.get("email")
          password = request.POST.get("password")
          confirm_password = request.POST.get("confirm_password")
          
          
          context = {
               "username" : username,
               "email" : email,
          }
          
          if not username  :
               messages.error(request,"username is required")
               return render(request,'signup.html',context)
          
          if password != confirm_password :
               messages.error(request,"password do not match ,check password")
               return render(request,'signup.html',context)
          
          if User.objects.filter(username=username).exists():
               messages.error(request,"user already exists,try another username")
               return render(request,'signup.html',context)
          
          User.objects.create_user(
          username = username, 
          email = email,
          password = password,           
          )
          
          messages.success(request,"Account created successfully")
          return redirect("login")
            
     return render(request,'signup.html')



 
def login_view(request):
     
     if request.method == "POST" :
          username = request.POST.get("username")
          password = request.POST.get("password")
          
          User = authenticate(request,username=username,password=password)
          if User is not None :
               login(request,User)
               return redirect("/")
          else:
               messages.error(request,"invalid username or password")
     
     return render(request,'login.html')





def logout_view(request):
     logout(request)
     return redirect ( "login")



@login_required(login_url="login")
def add_dream (request):
    
     if request.method == "POST":  
          dream  = request.POST.get("dream") 
          career = request.POST.get("career")
          effort = request.POST.get("effort")
          action =  request.POST.get("action")
          
          if action == "bucket" :
             dreams.objects.create(
               user = request.user,   
               dream = dream,
               career = career,
               effort = effort,
            )
           
          elif action =="dustbin": 
               dustbin_dreams.objects.create(
               user = request.user,     
               dream = dream,
               career = career,
               effort = effort,
            )
          
     return render (request,"add_dream.html")




@login_required(login_url="login")
def bucket (request):
     
  queryset = dreams.objects.filter(user = request.user)
  
  for dream in queryset :
     dream.jokes = get_random_jokes("bucket")
     
  context = {'dreams' : queryset}
  return render (request,'bucket.html',context)

 

@login_required(login_url="login")
def dustbin (request):
     
    queryset = dustbin_dreams.objects.filter(user = request.user)
    
    for dream in queryset :
     dream.jokes = get_random_jokes("dustbin")
    
     
    context = {'dustbin_dreams' : queryset}    
    return render (request,'dustbin.html',context)
 
 

 