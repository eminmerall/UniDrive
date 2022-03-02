"""uniDrive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views

import imagesapp
from bulut.views import home_view, login_view, register_view, hesap_view
from imagesapp.views import dosyalarim_view, file_storage_to_db, havuz_view, sil_view, duzenle_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('yukleme/', file_storage_to_db),
    path('dosyalarim/', dosyalarim_view),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    url('^accounts/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('havuz/', havuz_view),
    path('hesap/', hesap_view),
    path('yukleme/', include('imagesapp.urls')),

    path('sil/<int:dId>', sil_view),
    path('duzenle/<int:dId>', duzenle_view)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

