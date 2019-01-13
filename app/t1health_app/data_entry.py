from django import forms

from .models import Statistic

class StatisticForm(forms.ModelForm):

    class Meta:
        model = Statistic
        fields = ('title', 'text',)
