from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'bootstrap_practice_app/index.html')
