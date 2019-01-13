from django.http import *
from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect
from django.utils import timezone
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

# @login_required(login_url='/login_user/')
def input_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/input_page.html', {'inputs': inputs})

# @login_required(login_url='/login_user/')
def front_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/front_page.html', {'inputs': inputs})

# def main_loginpage(request):
#     return render(request, )
# def login_user(request):
#     logout(request)
#     username = password = ''
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#     return render(request, 't1health_app/login.html');
