from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import SignUpForm
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
def uyegiris(request):
    setting = Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request, 'uyegiris.html', context)
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def login_view(request):
    if request.method == 'POST':  # check post
            email = request.POST['email']
            password = request.POST['password']
            user=authenticate(request, email=email,password=password)
            if user is not None:
                return HttpResponseRedirect('/')
            else:
                messages.warning(request,"Hatalı kullanıcı adı veya parola girişi!")
                return HttpResponseRedirect('/login')
    return render(request,'login.html')

def signup_view(request):
    if request.method == 'POST':  # check post
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user=authenticate(email=email,password=password)
            login(request,user)
            return HttpResponseRedirect('/')
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)