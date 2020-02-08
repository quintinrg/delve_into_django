from django.shortcuts import render
from django.http import HttpResponse

# This function actually displays the text below. This is considered a "view"
x = "42"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. " + x)
