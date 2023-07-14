from django.shortcuts import render,redirect

def my_profile(request):
    return render(request,"myprofile.html")

def trys(request):
    return render(request,"try.html")
