from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Form,TryForm

# Register your models here.
@admin.register(Form)
class ShopAdmin(OSMGeoAdmin):
	list_display = ('PalikaName','Province','District','location')
	
@admin.register(TryForm)
class TryFormAdmin(OSMGeoAdmin):
	list_display=('enteredArea','enteredPalikaName','enteredSecretaryName')
