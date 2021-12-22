from django.shortcuts import render
from .forms import UsersForm,AttendForm
import datetime as dt
 

def new(request):
    params = {'form': None}
    params['form'] = AttendForm()
    return render(request, 'new.html', params)


def create(request):
    params = {'name': '','in_out':'','time': '','form': None}
    if request.method == 'POST':
        form = AttendForm(request.POST)
        params['name'] = request.POST['name']
        params['in_out'] = request.POST['in_out']
        obj=form.save(commit=False)
        obj.date=dt.datetime.now().date()
        obj.time=params['time']=dt.datetime.now().time()
        params['form'] = form

        if request.POST['in_out']=='出勤':
            obj.in_out="出勤"

        else:
            obj.in_out="退勤"

            
        if form.is_valid():
            form.save()
    else:
        params['form'] = UsersForm()

    return render(request, 'create.html', params)