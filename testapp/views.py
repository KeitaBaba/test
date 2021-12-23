from django.shortcuts import render
from .models import Attend
from .forms import AttendForm
import datetime as dt
from django.db.models import Q


#名前を選択式
#チェックボックス一つのみ選択
#日付や名前でフィルター
#ファイルで出力(csvかExcel)
#出勤時刻と退勤時刻を横並びで
#編集機能

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
        params['form'] = AttendForm()

    return render(request, 'create.html', params)


def list(request):
    List=Attend.objects.all()

    username = request.GET.get('name')
    attendtype = request.GET.get('type')
    hiduke= request.GET.get('hiduke')

    #名前で検索
    if username:
         List = List.filter(
                name__icontains=username
       )


    #出退勤で検索
    if attendtype:
         List = List.filter(
                in_out__icontains=attendtype
       )


    #日付で検索
    if hiduke=='一週間前':
        one_week_ago = dt.datetime.now() - dt.timedelta(days=7)
        List = List.filter(date__range=[one_week_ago, dt.datetime.now()])

    if hiduke=='当日':
        today=dt.datetime.now().strftime('%m-%d')
        List = List.filter(date__icontains=today)
      
    
    params={'List':List}
    return render(request,'list.html', params)
