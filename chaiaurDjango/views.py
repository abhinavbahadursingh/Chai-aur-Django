from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Home page")
    return render(request , "website/index.html")
def contact(request):
    return HttpResponse("contact page")
def about(request):
    return HttpResponse("about page")
def login(request):
    return HttpResponse("login page")
