from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'base.html')
def index(request):
    return HttpResponse("HI")
