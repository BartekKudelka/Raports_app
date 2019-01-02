from django import forms
from django.forms import ModelForm
from .models import Report


class CreateReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('start_date', 'end_date')
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control'})
        }
