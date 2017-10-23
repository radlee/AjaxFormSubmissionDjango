# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from gallery.models import Comments
from .forms import CommentForm
from django.http import JsonResponse

def index(request):
    form = CommentForm()
    if request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {
                'message' : 'form is saved'
            }
            return JsonResponse(data)

    context = {
        'name': 'Artful Dodger',
        'form': form,
    }

    return render(request, 'gallery/index.html',context)
