# Generated by Django 3.0.6 on 2020-05-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bulut', '0002_delete_kullanici'),
    ]

    operations = [
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('kId', models.AutoField(primary_key=True, serialize=False)),
                ('kOgrNo', models.CharField(db_column='Ogr_No', max_length=20, unique=True, verbose_name='Ogr_No')),
                ('kAd', models.CharField(db_column='Adı', max_length=50, verbose_name='Adı')),
                ('kSoyad', models.CharField(db_column='Soyadı', max_length=50, verbose_name='Soyadı')),
                ('kMail', models.EmailField(db_column='Email', max_length=254, verbose_name='E-Mail')),
                ('kOkul', models.CharField(db_column='Okul', max_length=200, null=True, verbose_name='Okul')),
                ('kBolum', models.CharField(db_column='Bölüm', max_length=200, null=True, verbose_name='Bölüm')),
            ],
        ),
    ]
