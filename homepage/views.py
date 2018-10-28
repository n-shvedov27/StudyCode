from django.shortcuts import render
from django.core.mail import send_mail


def send_email(request):
    user = request.POST['uname']
    dire = request.POST['direct_way']
    if dire == 0:
        dire = "Не определился"
    elif dire == 1:
        dire = "Мобильная разработка"
    else:
        dire = "Веб-разработка"
    mail = request.POST['email']
    messeage = "Имя - {}\nМайл - {}\nНаправление - {}".format(user, mail, dire)
    send_mail('Новый ученик', messeage, 'n.shvedov27@gmail.com',
              ['n.shvedov27@gmail.com'], fail_silently=False)
    return render(request, './index.html', locals())


def homepage(request):
    return render(request, './index.html', locals())


def about_us(request):
    return render(request, './about-us.html', locals())


1
