from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore


def index(request):
    request.session['key'] = 'value'
    context = {
        'session_key': request.session.get('key', None),
        'cookies': request.COOKIES
    }
    response = render(request, 'cookie_session_app/index.html', context)
    response.set_cookie('cookie', 'cookie-value')
    return response


def explore(request):
    request.session.delete()
    context = {
        'session_key': request.session.get('key', None),
        'cookies': request.COOKIES
    }
    return render(request, 'cookie_session_app/index.html', context)
