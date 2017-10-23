# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import SignUp

def index(request):
    context = {
        'name': 'lolito',
        'users': SignUp.objects.all()
    }
    return render(request, 'signup/index.html',context)



def create(request):
    if request.method == 'POST':
        user = SignUp.objects.creata(name = request.POST['name'], email = request.POST['email'])
        return redirect('main:index')
