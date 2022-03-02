# libraries are imported
# rendering the template using render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# this will be used to get the path of the media folder from settings
from django.conf import settings
# for storing the file in the desired folder, FileSystemStorage is used
from django.core.files.storage import FileSystemStorage
# this will handle MultiValueDictKeyError using try and except
from django.utils.datastructures import MultiValueDictKeyError
# using class from models.py
from imagesapp.models import dosya_havuz
from bulut.models import kullanici
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from http.client import responses

def havuz_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    kullanicilar = kullanici.objects.filter(kAd=username)
    dosyalar = dosya_havuz.objects.all()
    return render(request, "havuz.html", {'dosyalar': dosyalar})

def dosyalarim_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    dosyalar = dosya_havuz.objects.filter(kAd=username)
    return render(request, "dosyalarim.html", {'dosyalar': dosyalar})

# Create your views here.
def file_storage_to_db(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        kullanicilar = kullanici.objects.filter(kAd=username)

        file_path = settings.MEDIA_ROOT
        if request.method == 'POST':
            try:
                myFile = request.FILES['myFile']
            except MultiValueDictKeyError:
                print("Error.......")
                myFile = "None"
            fs = FileSystemStorage(location=file_path)
            filename = fs.save(myFile.name, myFile)
            file_url = fs.url(filename)

            q = dosya_havuz(
                dosyaAdı=request.POST.get("dosyaAdi"),
                dersAdi=request.POST.get("dersAdi"),
                aciklama=request.POST.get("aciklama"),
                bolumAdi=request.POST.get("bolumAdi"),
                okulAdi=request.POST.get("okulAdi"),
                kAd=username,
                file_name=filename,
                file_url=file_url,
            )
            q.save()
            return render(request, 'dosyalarim.html')
        else:
            return render(request, 'yukleme.html')

def sil_view(request, dId):
    q = dosya_havuz.objects.get(dId=dId)
    q.delete()
    return redirect('/dosyalarim')

def duzenle_view(request, dId):
    dosyam = dosya_havuz.objects.get(dId=dId)
    q = dosya_havuz.objects.get(dId=dId)
    if request.method == "POST":
        q.dosyaAdı = request.POST.get('dosyaAdı')
        q.dersAdi = request.POST.get('dersAdi')
        q.bolumAdi = request.POST.get('bolumAdi')
        q.okulAdi = request.POST.get('okulAdi')
        q.aciklama = request.POST.get('aciklama')
        q.save()
        return redirect('/dosyalarim')
    return render(request, "duzenle.html", {"dosya": dosyam})


