from django.db import models

# Create your models here.
from django.db import models


class kullanici(models.Model):
    id = models.AutoField(primary_key=True)
    kAd = models.CharField(max_length=20, verbose_name='Kullanıcı Adı', db_column='Kullanıcı Adı', unique=True)
    ogrNo = models.CharField(max_length=20, verbose_name='Öğrenci No', db_column='Öğrenci No', null=True)
    adi = models.CharField(max_length=50, verbose_name='Adı', db_column='Adı', null=True)
    soyadi = models.CharField(max_length=50, verbose_name='Soyadı', db_column='Soyadı', null=True)
    mail = models.EmailField(verbose_name='E-Mail', db_column='Email')
    okul = models.CharField(max_length=200, verbose_name='Okul', db_column='Okul', null=True)
    bolum = models.CharField(max_length=200, verbose_name='Bölüm', db_column='Bölüm', null=True)
