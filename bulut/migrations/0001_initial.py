# Generated by Django 3.0.6 on 2020-05-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('kId', models.AutoField(primary_key=True, serialize=False)),
                ('kOgrNo', models.CharField(db_column='Ogr_No', max_length=20, unique=True, verbose_name='Ogr_No')),
                ('kAdSoyad', models.CharField(db_column='AdıSoyadı', max_length=100, verbose_name='AdıSoyadı')),
                ('kMail', models.EmailField(db_column='Email', max_length=254, verbose_name='E-Mail')),
                ('kOkul', models.CharField(db_column='Okul', max_length=200, null=True, verbose_name='Okul')),
                ('kBolum', models.CharField(db_column='Bölüm', max_length=200, null=True, verbose_name='Bölüm')),
            ],
        ),
    ]