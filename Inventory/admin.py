from django.contrib import admin
from .models import *
from import_export.admin  import ImportExportModelAdmin
# Register your models here.
# admin.site.register(Desktop,Laptop,Mobile)
@admin.register(Desktop,Laptop,Mobile)
# class ViewAdmin(admin.ModelAdmin):
#     pass

class ViewAdmin(ImportExportModelAdmin):
    pass