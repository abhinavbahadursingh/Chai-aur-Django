from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello you are at abhinav learning")
    return render(request , 'website/index.html')
def about(request):
    return HttpResponse("this is about")
def contact(request):
    return HttpResponse("this is contact")