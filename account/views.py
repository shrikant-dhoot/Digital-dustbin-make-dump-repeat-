from django.http import HttpResponse
from django.shortcuts import render , redirect,get_object_or_404
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
             messages.success(request,"dream add  successfully! into bucket " )
           
          elif action =="dustbin": 
               dustbin_dreams.objects.create(
               user = request.user,     
               dream = dream,
               career = career,
               effort = effort,
            )
               messages.success(request,"dream remove successfully! into dustbin " )
          
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




@login_required(login_url="login")
def bucket_action (request):
     if request.method =="POST":
          dream_id = request.POST.get("dream_id")
          action =  request.POST.get("action")
          
          dream = get_object_or_404(dreams,id=dream_id,user=request.user)
          
          if action=="complete":
               
               dream.completed = True
               dream.save()   
               messages.success(request,"dream achieve successfully !" )
               
          elif action == "give up":
               
            dustbin_dreams.objects.create(
               user = request.user,     
               dream = dream.dream,
               career = dream.career,
               effort = dream.effort,
            )
            
            dream.delete()
            messages.warning(request,"dream moved to dustbin")
            
            
          elif action == "delete":
               dream.delete()
               messages.warning(request,"Dream deleted permanently")
                 
     return redirect("bucket")



@login_required(login_url="login")
def dustbin_action(request):
     
     if request.method =="POST":
      dream_id = request.POST.get("dream_id")
      action =  request.POST.get("action")
          
      dream = get_object_or_404(dustbin_dreams,id=dream_id,user=request.user)
      
      if action == "delete":
          dream.delete()
          messages.success(request,"dream permanetly deleted")
            
     return redirect("dustbin")
                 
          
               
 
def dasboard(request):
     
     total_dream = dreams.objects.filter(user = request.user).count()
     completed = dreams.objects.filter(user = request.user,completed = True).count()
     bucket    = dreams.objects.filter(user = request.user,completed = False).count()
     dustbin   = dustbin_dreams.objects.filter(user = request.user).count()
     
     
     if total_dream > 0:
          progress = int((completed / total_dream)*100)
     else :
          progress = 0      
     
     context = {
          "total_dream" : total_dream,
          "completed" : completed,
          "bucket" : bucket,
          "dustbin" : dustbin , 
          "progress" : progress 
     }
     
     
     return render(request,'dasboard.html',context)         

 