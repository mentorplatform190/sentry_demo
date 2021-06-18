from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    x = 1/0
    return HttpResponse("Hello, world. You're at the polls index.")
