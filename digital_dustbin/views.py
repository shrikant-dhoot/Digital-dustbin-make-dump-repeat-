from django.http import HttpResponse
from django.shortcuts import render 



def home (request):
    return render (request,'home.html')

def add_dream (request):
    return render (request,"add_dream.html")

def bucket (request):
    return render (request,'bucket.html')

def dustbin (request):
    return render (request,'dustbin.html')