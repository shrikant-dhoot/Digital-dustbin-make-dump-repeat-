from django.http import HttpResponse
from django.shortcuts import render 



def home (request):
    return render (request,'home.html')

def add_dream (request):
    return render (request,"add_dream.html")