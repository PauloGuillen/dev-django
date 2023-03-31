# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    raise ValueError
    return HttpResponse('<HTML><BODY>olá Django</BODY></HTML>', content_type='text/html')
