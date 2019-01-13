from django import forms
from django.forms import ModelForm
from .models import Statistic

class StatisticForm(ModelForm):
  
  class Meta:
    model = Statistic
    # fields = '__all__' # Or a list of the fields that you want to include in your form
    fields = ('weight', 'bmi', 'nutrition', 'exercise',)
