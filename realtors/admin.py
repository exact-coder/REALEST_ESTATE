from django.contrib import admin
from .models import *


# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','date_hired')
    list_display_links = ('id','name')
    search_fields = ('name','id')
    list_per_page = 20

admin.site.register(Realter,RealtorAdmin)

