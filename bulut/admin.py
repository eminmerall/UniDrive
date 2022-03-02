from django.contrib import admin
from .models import kullanici

# Register your models here.
class adminKullanici(admin.ModelAdmin):
    class Meta:
        model = kullanici

admin.site.register(kullanici, adminKullanici)
