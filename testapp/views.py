from django.shortcuts import render
from .models import Attend
from .forms import UsersForm,AttendForm
import datetime as dt
from django.db.models import Q


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

    keyword1 = request.GET.get('keyword1')
    keyword2 = request.GET.get('keyword2')
    hiduke= request.GET.get('hiduke')

    if hiduke=='一週間前':
        one_week_ago = dt.datetime.now() + dt.timedelta(days=7)
        List = List.filter(date__range=[one_week_ago, dt.datetime.now()])

    if hiduke=='当日':
        today = dt.datetime.now()
        List = List.filter(date__icontains=today)

    #if keyword2 and keyword2:
    #   List = List.filter(
    #            name__icontains=keyword1,in_out__icontains=keyword2
    #   )
    
    params={'List':List}
    return render(request,'list.html', params)
