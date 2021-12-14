from django.shortcuts import render
from .forms import UsersForm
 

def new(request):
    params = {'form': None}
    params['form'] = UsersForm()
    return render(request, 'new.html', params)


def create(request):
    params = {'name': '', 'email': '', 'address': '','form': None}
    if request.method == 'POST':
        form = UsersForm(request.POST)
        params['name'] = request.POST['name']
        params['email'] = request.POST['mail']
        params['address'] = request.POST['address']
        params['form'] = form
        if form.is_valid():
            form.save()
    else:
        params['form'] = UsersForm()
    return render(request, 'create.html', params)