from django.shortcuts import render


def ask(request):
    return render(request, './faq.html', locals())
