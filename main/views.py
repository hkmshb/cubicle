from django.shortcuts import render
from django.http.response import HttpResponse



def home_page(request):
    return HttpResponse('Cubicle !*')