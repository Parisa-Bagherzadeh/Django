from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def test(request):
    return HttpResponse("<h4> This is a test! </h4>")