from django.contrib import admin
from . models import dosya_havuz

# Model is registered here.
class adminHavuz(admin.ModelAdmin):
    list_display = ["kAd", "dosyaAdı", "olusturma", "okulAdi", "bolumAdi"]
    list_display_links = ["kAd", "dosyaAdı", "olusturma", "okulAdi", "bolumAdi"]
    list_filter = ["olusturma", "okulAdi", "bolumAdi"]
    search_fields = ["kAd", "DosyaAdı", "okulAdi", "bolumAdi"]

    class Meta:
        model = dosya_havuz

admin.site.register(dosya_havuz, adminHavuz)
