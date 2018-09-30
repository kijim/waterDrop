from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeCardTable, User
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils import timezone
from waterDrop import settings
from django.core.mail import send_mail, EmailMessage

'''
ログインに関してはここが役に立つ
https://it-engineer-lab.com/archives/544
'''
# Create your views here.
@login_required
def main(request):
    '''ログイン画面表示'''

    return render(request, 'waterDropApp/index.html')

'''
ログイン画面表示
'''
def login(request):
    print("hello login")
    return render(request, 'waterDropApp/login.html',{})

'''
出勤画面表示
'''
@login_required
def timeCard(request):
    '''表示オンリー'''
    try:
        '''現在日時を取得する'''
        nowDate = timezone.localtime().strftime("%Y-%m-%d")
        '''ここをユーザー名指定にしないとやばい'''
        record = TimeCardTable.objects.get(date=nowDate)
        inTime = record.getInTime()[0:5]
        offTime = record.getOffTime()[0:5]
        if inTime != "None":
           offTime = timezone.localtime().strftime("%H:%M")
    except TimeCardTable.DoesNotExist:
        '''まだ未入力なので現在時刻を出社時刻に設定する'''
        inTime = timezone.localtime().strftime("%H:%M")

    form = forms.TimeCardForm(initial={'inTime': inTime, 'offTime': offTime,
                                       'username': request.user.username,
                                       'date': nowDate})

    return render(request, 'waterDropApp/timecard.html', {"form": form})

'''
出退勤時間を登録する
'''
def timeCardEntry(request):
    offTime = ""
    inTime = ""
    if request.method == "POST":
        '''出社時間、退社時間を登録'''
        form = forms.TimeCardForm(request.POST)
        if form.is_valid():
            '''ユーザテーブルからユーザIDを取得する'''
            username = form.cleaned_data['username']
            employee_id = User.objects.get(username=username)

            '''日付とユーザIDからタイムカードの主キーを取得する'''
            pk = TimeCardTable.objects.get(date=form.cleaned_data['date'], employee_id=employee_id)
            print(pk.id)
            TimeCardTable(id = pk.id, employee_id = employee_id, date = form.cleaned_data['date'],
                          inTime=form.cleaned_data['inTime'], offTime = form.cleaned_data['offTime']).save()
        else:
            '間違い'
            print("error happen")
    return render(request, 'waterDropApp/timecard_entry.html')

'''メール送信テスト'''
def mail(request):
    subject = "題名"
    message = "本文\\nです"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [
        "konickcioc@gmail.com"
    ]
    send_mail(subject, message, from_email, recipient_list)
    return render(request, 'waterDropApp/mail.html')
