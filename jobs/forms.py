from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary', 'description']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'resume']