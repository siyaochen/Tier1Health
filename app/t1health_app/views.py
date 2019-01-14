from django.http import *
from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect, get_object_or_404
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
from django.views.generic.base import RedirectView
from .fusioncharts import FusionCharts
from collections import OrderedDict
from .forms import StatisticForm


# os.environ["MY_PHONE_NUMBER"]

def results_weight_page(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Weight Statistics",
            "xAxisName": "Day",
            "yAxisName": "Kg",
            "theme": "zune"
        }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in Statistic.objects.all():
      data = {}
    #   data['label'] = key.weight
      data['value'] = key.weight
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
    return render(request, 't1health_app/weight.html', {'output': column2D.render()})

def results_bmi_page(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "BMI Statistics",
            "xAxisName": "Day",
            "yAxisName": "kg/m^2",
            "theme": "zune"
        }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in Statistic.objects.all():
      data = {}
    #   data['label'] = key.weight
      data['value'] = key.bmi
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-2", "json", dataSource)
    return render(request, 't1health_app/bmi.html', {'output': column2D.render()})

def results_nutrition_page(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Nutrition Statistics",
            "xAxisName": "Day",
            "yAxisName": "kcal",
            "theme": "zune"
        }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in Statistic.objects.all():
      data = {}
    #   data['label'] = key.weight
      data['value'] = key.nutrition
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-3", "json", dataSource)
    return render(request, 't1health_app/nutrition.html', {'output': column2D.render()})

def results_exercise_page(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Exercise Statistics",
            "xAxisName": "Day",
            "yAxisName": "Minutes",
            "theme": "zune"
        }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in Statistic.objects.all():
      data = {}
    #   data['label'] = key.weight
      data['value'] = key.exercise
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-4", "json", dataSource)
    return render(request, 't1health_app/exercise.html', {'output': column2D.render()})

favicon_view = RedirectView.as_view(url='/static/t1health_app/images/favicon.ico', permanent=True)

def send_message_weight(sid, token, name):

    client = Client(sid, token)
    client.messages.create(
        to = environ.os["MY_PHONE_NUMBER"],
        from_ = "+16476967454",
        body = "\nHey, your latest weight total was " + str(name) + " kg.\nGood Work! Keep on exercising and improving overall health!"
    )

def send_messagefunc_weight(request):
    if request.method == 'GET':
        account_sid = environ.os["TWILIO_ACCOUNT_SID"]
        auth_token = environ.os["TWILIO_AUTH_TOKEN"]
        cur_time = str(datetime.now())
        # dataSource['data'] = []
        for key in Statistic.objects.all():
            name = key.weight

        # Retrieve name and whether user updated from database here
        updated = False
        # name = ""
            # if (not updated and (cur_time[12:14] == "22" or cur_time[12:14] == "24") and cur_time[15:17] == "00"):
        send_message_weight(account_sid, auth_token, name)
            # time.sleep(60)
        return render(request, 't1health_app/front_page.html')
    else:
        return redirect('/front_page.html/')
def send_message_exercise(sid, token, name):

    client = Client(sid, token)
    client.messages.create(
        to = environ.os["MY_PHONE_NUMBER"],
        from_ = "+16476967454",
        body = "\nHey, your latest exercise total was " + str(name) + " min.\nGood Work! Keep on exercising and improving overall health!"
    )

def send_messagefunc_exercise(request):
    if request.method == 'GET':
        account_sid = environ.os["TWILIO_ACCOUNT_SID"]
        auth_token = environ.os["TWILIO_AUTH_TOKEN"]
        cur_time = str(datetime.now())
        # dataSource['data'] = []
        for key in Statistic.objects.all():
            name = key.exercise

        # Retrieve name and whether user updated from database here
        updated = False
        # name = ""
            # if (not updated and (cur_time[12:14] == "22" or cur_time[12:14] == "24") and cur_time[15:17] == "00"):
        send_message_exercise(account_sid, auth_token, name)
            # time.sleep(60)
        return render(request, 't1health_app/front_page.html')
    else:
        return redirect('/front_page.html/')

def send_message_bmi(sid, token, name):

    client = Client(sid, token)
    client.messages.create(
        to = environ.os["MY_PHONE_NUMBER"],
        from_ = "+16476967454",
        body = "\nHey, your latest bmi total was " + str(name) + " kg/m^2.\nGood Work! Keep on exercising and improving overall health!"
    )

def send_messagefunc_bmi(request):
    if request.method == 'GET':
        account_sid = environ.os["TWILIO_ACCOUNT_SID"]
        auth_token = environ.os["TWILIO_AUTH_TOKEN"]
        cur_time = str(datetime.now())
        # dataSource['data'] = []
        for key in Statistic.objects.all():
            name = key.bmi

        # Retrieve name and whether user updated from database here
        updated = False
        # name = ""
            # if (not updated and (cur_time[12:14] == "22" or cur_time[12:14] == "24") and cur_time[15:17] == "00"):
        send_message_bmi(account_sid, auth_token, name)
            # time.sleep(60)
        return render(request, 't1health_app/front_page.html')
    else:
        return redirect('/front_page.html/')

def send_message_nutrition(sid, token, name):

    client = Client(sid, token)
    client.messages.create(
        to = environ.os["MY_PHONE_NUMBER"],
        from_ = "+16476967454",
        body = "\nHey, your latest nutrition total was " + str(name) + " kcal.\nGood Work! Keep on exercising and improving overall health!"
    )

def send_messagefunc_nutrition(request):
    if request.method == 'GET':
        account_sid = environ.os["TWILIO_ACCOUNT_SID"]
        auth_token = environ.os["TWILIO_AUTH_TOKEN"]
        cur_time = str(datetime.now())
        # dataSource['data'] = []
        for key in Statistic.objects.all():
            name = key.nutrition

        # Retrieve name and whether user updated from database here
        updated = False
        # name = ""
            # if (not updated and (cur_time[12:14] == "22" or cur_time[12:14] == "24") and cur_time[15:17] == "00"):
        send_message_nutrition(account_sid, auth_token, name)
            # time.sleep(60)
        return render(request, 't1health_app/front_page.html')
    else:
        return redirect('/front_page.html/')

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
# def input_page(request):
#     inputs = Statistic.objects.all()
#     return render(request, 't1health_app/input_page.html', {'inputs': inputs})

def fitness_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/fitness.html', {'inputs': inputs})

def nutrition_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/nutrition.html', {'inputs': inputs})

# def stats_page(request):
#     inputs = Statistic.objects.all()
#     return render(request, 't1health_app/stats.html', {'inputs': inputs})

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

def statistic_new(request):
    # statistic = get_object_or_404(Statistic)
    if request.method == "POST":
        form = StatisticForm(request.POST)
        if form.is_valid():
            statistic = form.save(commit=False)
            statistic.author = request.user
            statistic.save()
            return redirect('results_weight_page', pk=post.pk)
    else:
        form = StatisticForm()
    return render(request, 't1health_app/input_page.html', {'form' : form})
    # return render(request, 't1health_app/input_page.html', {'form' : form})

def statisticinput(request):
    if request.method == "POST":
        form = StatisticForm(request.POST)
        if form.is_valid():
            statistic = form.save(commit=False)
            statistic.author = request.user
            statistic.save()
            return redirect('results_weight_page')
    else:
        form = StatisticForm()
    return render(request, 't1health_app/input_page.html', {'form' : form})

    # form = StatisticForm()
    # return render(request, 't1health_app/input_page.html', {'form': form})
