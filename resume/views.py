from django.shortcuts import render

def new(request):
    return render(request,"resume/new.html")

def msc(request):
    return render(request,"resume/msc.html")

def bsc(request):
    return render(request,"resume/bsc.html")