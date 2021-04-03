from django.http import HttpResponse
from django.shortcuts import render
import urllib
import urllib.request

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


def checkHTML(request):
    webUrl = urllib.request.urlopen("https://www.guru99.com/accessing-internet-data-with-python.html")
    data = webUrl.read()
    print(data)
    return HttpResponse(data)
