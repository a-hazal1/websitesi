from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, ContactFormMessage
from home.models import Setting, ContactFormu


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
    if request.method == 'POST':  # check post
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.number = form.cleaned_data['number']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
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
def login(request):
    setting = Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'login.html', context)
