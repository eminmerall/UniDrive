from django.db import models
from datetime import datetime
# from bulut.models import kullanici

# Create your models here.
# I have used three fields/columns/attributes of the class

""" file_name: To save the name of file to be uploaded by the user.
	file_url: To save the url of the location where the file is to be saved.
	last_update: to store date and time. Automatically set the field to now every time the object is saved using auto_now = True
"""

class dosya_havuz(models.Model):
    dId = models.AutoField(primary_key=True, verbose_name='Dosya ID', db_column='Dosya ID')
    kAd = models.CharField(max_length=255, verbose_name='Kullanıcı Adı', db_column='Kullanıcı Adı', null=True)
    dersAdi = models.CharField(max_length=255, verbose_name='Ders Adı', db_column='Ders Adı', null=True)
    okulAdi = models.CharField(max_length=255, verbose_name='Okul Adı', db_column='Okul Adı', null=True)
    bolumAdi = models.CharField(max_length=255, verbose_name='Bölüm Adı', db_column='Bölüm Adı', null=True)
    aciklama = models.CharField(max_length=255, verbose_name='Açıklama', db_column='Açıklama', null=True)
    dosyaAdı = models.CharField(max_length=255, verbose_name='Dosya Adı', db_column='Dosya Adı', null=True)
    olusturma = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi", db_column="Oluşturma Tarihi", null=True)
    file_name = models.CharField(max_length=255, verbose_name='Adı', db_column='Adı')
    file_url = models.TextField(verbose_name='Dosya URL', db_column='Dosya URL')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme', db_column='Son Güncelleme')

    def __str__(self):
        return self.file_name

