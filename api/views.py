from django.shortcuts import render
from django.http import HttpResponse

# Create your views (endpoint) here.


def main(request):
    return HttpResponse("Hello")      