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
def myFirstChart(request):

    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Country"
    chartConfig["yAxisName"] = "Reserves (MMbbl)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
    chartData = OrderedDict()
    chartData["Venezuela"] = 290
    chartData["Saudi"] = 260
    chartData["Canada"] = 180
    chartData["Iran"] = 140
    chartData["Russia"] = 115
    chartData["UAE"] = 100
    chartData["US"] = 30
    chartData["China"] = 30

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array 
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
    data["label"] = key
    data["value"] = value
    dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

    return render(request, 't1health_app/input_page.html', {
    'output': column2D.render()
})

favicon_view = RedirectView.as_view(url='/static/t1health_app/images/favicon.ico', permanent=True)

def send_message(sid, token, name):
    client = Client(sid, token)
    client.messages.create(
        to = +14162588389,
        from_ = "+16476967454",
        body = "\nHey" + name + "\nRemember to enter your diet and measured weight for today!"
    )

def send_messagefunc(request):
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
# def input_page(request):
#     inputs = Statistic.objects.all()
#     return render(request, 't1health_app/input_page.html', {'inputs': inputs})

def fitness_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/fitness.html', {'inputs': inputs})

def nutrition_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/nutrition.html', {'inputs': inputs})

def results_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/results.html', {'inputs': inputs})

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
            return redirect('results_page', pk=post.pk)
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
            return redirect('results_page')
    else:
        form = StatisticForm()
    return render(request, 't1health_app/input_page.html', {'form' : form})

    # form = StatisticForm()
    # return render(request, 't1health_app/input_page.html', {'form': form})
