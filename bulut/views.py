from django.shortcuts import render, redirect
from .forms import loginForm, registerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import kullanici
# Create your views here.

def home_view(request):
    return render(request, "home.html", {})

def login_view(request):
    form = loginForm(request.POST or None)
    return render(request, "registration/login.html", {})

def hesap_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    kullanicilar = kullanici.objects.filter(kAd=username)

    if kullanici.objects.filter(kAd=username):
        q = kullanici.objects.get(kAd=username)
        if request.method == 'POST':
            q.ogrNo = request.POST.get('ogrNo')
            q.adi = request.POST.get('adi')
            q.soyadi = request.POST.get('soyadi')
            q.mail = request.POST.get('mail')
            q.okul = request.POST.get('okul')
            q.bolum = request.POST.get('bolum')
            q.save()
            return redirect('/hesap')
    return render(request, "hesap.html", {'kullanicilar': kullanicilar})

def register_view(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        q = kullanici(
            kAd=request.POST.get("username"),
            mail=request.POST.get("email"),
        )
        q.save()
        login(request, new_user)
        return redirect('/hesap')
    return render(request, "registration/register.html")

