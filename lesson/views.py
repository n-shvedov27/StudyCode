from django.shortcuts import render


def web(request):
    return render(request, './web.html', locals())


def mobile(request):
    return render(request, './mobile.html', locals())
