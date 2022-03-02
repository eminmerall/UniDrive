from . import views
from django.urls import path
from . views import file_storage_to_db

# At thia url, one will redirect to views function file_storage_to_db which will serve request
# name is important when one has to redirect to some other page from current page

urlpatterns = [
              path('yukleme/', views.file_storage_to_db, name = 'file_storage_to_db')
    ]
