# Generated by Django 3.0.6 on 2020-05-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bulut', '0005_delete_kullanici'),
    ]

    operations = [
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('klAdı', models.CharField(db_column='Kullanıcı Adı', max_length=20, unique=True, verbose_name='Kullanıcı Adı')),
                ('OgrNo', models.CharField(db_column='Öğrenci No', max_length=20, null=True, verbose_name='Öğrenci No')),
                ('Ad', models.CharField(db_column='Adı', max_length=50, null=True, verbose_name='Adı')),
                ('Soyad', models.CharField(db_column='Soyadı', max_length=50, null=True, verbose_name='Soyadı')),
                ('Mail', models.EmailField(db_column='Email', max_length=254, verbose_name='E-Mail')),
                ('Okul', models.CharField(db_column='Okul', max_length=200, null=True, verbose_name='Okul')),
                ('Bolum', models.CharField(db_column='Bölüm', max_length=200, null=True, verbose_name='Bölüm')),
            ],
        ),
    ]
