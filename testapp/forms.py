from django import forms
from .models import Users,Attend
 
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        #fields = ('name', 'mail','address', )
        #labels = {'name':'名前', 'mail':'メールアドレス', 'address':'住所'}
        fields = ('name', 'address')
        labels = {'name':'名前'}


class AttendForm(forms.ModelForm):
    class Meta:
        model = Attend
        fields = ('name',)
        labels = {'name':'名前'}