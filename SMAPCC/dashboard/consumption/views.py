# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def summary(request):
    context = {
        # I understand the basics of the summary.html template, but as I've not learned how to integrate graphs into views.py I have left it as is.
        'message': 'This is where I would display graphs of user data.',
    }
    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)
