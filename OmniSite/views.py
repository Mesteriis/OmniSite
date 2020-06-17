from django.shortcuts import render, Http404
from django.http import HttpResponse


def index(request):
    template = 'index.html'
    content = {

    }
    return render(request, 'index.html', content)


def signIn(request):
    template = 'SignIn.html'
    content = {

    }
    return render(request, template, content)


def joinAs(request):
    template = 'join.html'
    content = {

    }
    return render(request, template, content)