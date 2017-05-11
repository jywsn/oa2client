# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def logout_view(request):
    """Redirect here after revoking token."""
    logout(request)  
    return redirect(settings.LOGOUT_REDIRECT_URL)

def index(request):
    if request.user.is_authenticated():
        return redirect('/home/')
    else:
        return render(request, 'login.html', {
            'next': request.GET.get('next', settings.LOGIN_REDIRECT_URL)
        })
  
@login_required
def home(request):
    return render(request, 'home.html', {})
 
@login_required
def other(request):
    return render(request, 'other.html', {})
