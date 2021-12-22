from django.shortcuts import render
from .models import Attend
from .forms import UsersForm,AttendForm
import datetime as dt


#名前を選択式
#チェックボックス一つのみ選択
#日付や名前でフィルター
#ファイルで出力(csvかExcel)
#出勤時刻と退勤時刻を横並びで
  

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


def list(request):
    List=Attend.objects.all()
    params={'List':List}
    return render(request,'list.html', params)
