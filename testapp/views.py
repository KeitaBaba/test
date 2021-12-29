from typing import List
from django.shortcuts import redirect, render
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
    
    return render(request, 'new.html')


def create(request):

    if request.method == 'POST':
        form = AttendForm(request.POST)
        name=request.POST['name']
        in_out=request.POST['in_out']
        obj=form.save(commit=False)
        obj.date=dt.datetime.now().date()
        obj.time=time=dt.datetime.now().time()
        

        if in_out=='出勤':
            rowcount=Attend.objects.all().filter(name=name,date=dt.datetime.now().date()).count()
            if rowcount==0:
                if form.is_valid():
                    form.save()

            else:
                return render(request, 'error.html')


        elif in_out=='退勤':
            attend=Attend.objects.get(name=name,date=dt.datetime.now().date())
            attend.leavetime=dt.datetime.now().time()
            attend.save()

    params = {
        'name' : name,
        'time' : time,
        'in_out' : in_out,
    }
    return render(request, 'create.html',params)



def list(request):

    List=Attend.objects.all()

    username = request.GET.get('name')
    hiduke= request.GET.get('hiduke')

    #名前で検索
    if username:
         List = List.filter(
                name__icontains=username
       )


    #日付で検索
    if hiduke=='一週間':
        one_week_ago = dt.datetime.now() - dt.timedelta(days=7)
        List = List.filter(date__range=[one_week_ago, dt.datetime.now()])

    if hiduke=='当日':
        today=dt.datetime.now().strftime('%m-%d')
        List = List.filter(date__icontains=today)
      
    
    params={'List':List}
    return render(request,'list.html', params)

def delete(request,pk):
    attend  = Attend.objects.filter(id=pk)
    attend.delete()


    return redirect('list')

def update(request,pk):

    attend  = Attend.objects.get(id=pk)
    if request.method == "POST":
        attend.name = request.POST["name"]
        attend.time = request.POST["in"]
        attend.leavetime = request.POST['out']
        attend.save()
        return redirect(list)

    else:
        params={'attend' : attend}
        return render(request, 'update.html',params)


