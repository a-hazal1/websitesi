from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'eski.html', context)
def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'hakkimizda.html', context)
def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'iletisim.html', context)
def fotograflarimiz(request):
    setting = Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'fotograflarimiz.html', context)
def blog(request):
    setting = Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'blog.html', context)
