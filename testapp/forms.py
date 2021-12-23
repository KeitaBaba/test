from django import forms
from .models import Attend
 



class AttendForm(forms.ModelForm):
    class Meta:
        model = Attend
        fields = ('name',)
        labels = {'name':'名前'}