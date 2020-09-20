# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from community.forms import *
from django.shortcuts import render

def write(request):
    if request.method=="POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    
    return render(request, 'write.html', {'form':form})

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html' ,{'articleList':articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})

def index(request):
    return render(request, 'index.html')

def shopping(request):
    return render(request, 'shopping.html')