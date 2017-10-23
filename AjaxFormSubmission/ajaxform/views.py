# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ajaxform.models import TinyTest
from .forms import TinyFormTest
from django.http import JsonResponse

def index(request):
    form = TinyFormTest()
    if request.is_ajax():
        form = TinyFormTest(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {
                'message' : 'form is saved'
            }
            return JsonResponse(data)

    context = {
        'name': 'General',
        'form': form,
    }

    return render(request, 'ajaxform/form.html',context)
