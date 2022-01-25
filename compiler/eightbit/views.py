from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'eightbit/index.html')