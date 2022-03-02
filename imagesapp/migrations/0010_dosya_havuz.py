# Generated by Django 3.0.6 on 2020-05-29 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesapp', '0009_delete_dosya_havuz'),
    ]

    operations = [
        migrations.CreateModel(
            name='dosya_havuz',
            fields=[
                ('dId', models.AutoField(db_column='Dosya ID', primary_key=True, serialize=False, verbose_name='Dosya ID')),
                ('kAd', models.CharField(db_column='Kullanıcı Adı', max_length=255, null=True, verbose_name='Kullanıcı Adı')),
                ('dersAdi', models.CharField(db_column='Ders Adı', max_length=255, null=True, verbose_name='Ders Adı')),
                ('okulAdi', models.CharField(db_column='Okul Adı', max_length=255, null=True, verbose_name='Okul Adı')),
                ('bolumAdi', models.CharField(db_column='Bölüm Adı', max_length=255, null=True, verbose_name='Bölüm Adı')),
                ('aciklama', models.CharField(db_column='Açıklama', max_length=255, null=True, verbose_name='Açıklama')),
                ('file_name', models.CharField(db_column='Dosya Adı', max_length=255, verbose_name='Dosya Adı')),
                ('file_url', models.TextField(db_column='Dosya URL', verbose_name='Dosya URL')),
                ('last_update', models.DateTimeField(auto_now=True, db_column='Son Güncelleme', verbose_name='Son Güncelleme')),
            ],
        ),
    ]