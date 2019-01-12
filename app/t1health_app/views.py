from django.shortcuts import render
from django.utils import timezone
from .models import Statistic

def input_page(request):
    inputs = Statistic.objects.all()
    return render(request, 't1health_app/input_page.html', {'inputs': inputs})
