from django.http import HttpResponse
from django.shortcuts import render
from.models import * 
from.utils import *

# Create your views here.

def signup(request):
     return render(request,'signup.html')
 
def login_view(request):
     return render(request,'login.html')

def logout_view(request):
     pass

def add_dream (request):
     if request.method == "POST":
          dream  = request.POST.get("dream") 
          career = request.POST.get("career")
          effort = request.POST.get("effort")
          action =  request.POST.get("action")
          
          if action == "bucket" :
          
           dreams.objects.create(
               dream = dream,
               career = career,
               effort = effort,
            )
           
          elif action =="dustbin": 
               dustbin_dreams.objects.create(
               dream = dream,
               career = career,
               effort = effort,
            )
          
          
     return render (request,"add_dream.html")


def bucket (request):
     
  queryset = dreams.objects.all()
  
  
  for dream in queryset :
     dream.jokes = get_random_jokes("bucket")
     
     context = {'dreams' : queryset}
  return render (request,'bucket.html',context)




def dustbin (request):
     
    queryset = dustbin_dreams.objects.all()
    
    for dream in queryset :
     dream.jokes = get_random_jokes("dustbin")
    
    context = {'dustbin_dreams' : queryset}    
    return render (request,'dustbin.html',context)
 
 

 