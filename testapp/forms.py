from django import forms
from .models import Users
 
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'mail','address', )
        labels = {'name':'名前', 'mail':'メールアドレス', 'address':'住所'}