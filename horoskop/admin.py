from django.contrib import admin
from .models import Horoskop


class HoroskopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("znak", )}


# Register your models here.
admin.site.register(Horoskop, HoroskopAdmin)
