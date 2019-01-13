from django.http import *
from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect
from django.utils import timezone
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
import subprocess
import os
import time
from datetime import datetime
from twilio.rest import Client
# os.environ["MY_PHONE_NUMBER"]

def send_message(sid, token, name):
    client = Client(sid, token)
    client.messages.create(
        to = +14162588389,
        from_ = "+16476967454",
        body = "\nHey" + name + "\nRemember to enter your diet and measured weight for today!"
    )

def send_messagefunc(request, username):
    if request.method == 'GET':
        account_sid = "ACac4b4ad89b8e8c0c75cabce115e5e841"
        auth_token = "1c09620916081dd7ad9a3cd11d25a558"
        cur_time = str(datetime.now())

        # Retrieve name and whether user updated from database here
        updated = False
        name = username
            # if (not updated and (cur_time[12:14] == "22" or cur_time[12:14] == "24") and cur_time[15:17] == "00"):
        send_message(account_sid, auth_token, name)
            # time.sleep(60)
        return render(request, 't1health_app/front_page.html')
    else:
        return redirect('/')
# from flask import Flask, request
# from twilio import twiml

# app = Flask(__name__)
# @app.route("/sms", methods=['POST'])

# def sms():
#     number = request.form['From']
#     message_body = request.form['Body']

#     resp = twmil.Response()
#     resp.message('Hello {}, you said: {}'.format(number, message_body))
#     return str(resp)

# def smsmessagefunc(request):
#     app.run()
#     return render(request, 't1health_app/front_page.html', {'inputs': inputs})

# @login_required(login_url='/login_user/')
def input_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/input_page.html', {'inputs': inputs})

# @login_required(login_url='/login_user/')
def front_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/front_page.html', {'inputs': inputs})

def submit(request):
    info=request.POST['info']
    return render(request, 't1health_app/input_page.html', {'inputs': inputs})

def your_view_name(request):
  if request.method == 'GET':
    form = your_form_name() 
  else:
    if form.is_valid():
      info = request.POST['info_name']
      output = script_function(info) 
      # Here you are calling script_function, 
      # passing the POST data for 'info' to it;
      return render(request, 't1health_app/front_page.html', {
        'info': info,
        'output': output,
      })
  return render(request, 't1health_app/front_page.html', {
    'form': form,
  })

  def script_function(post_from_form):
    return subprocess.check_call(['test.py', post_from_form])  

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
