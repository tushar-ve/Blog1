from django.contrib import admin
from .models import *
# Register your models here.
class ContactusAdmin(admin.ModelAdmin):
    list_display=['name','email','message']

admin.site.register(ContactModel,ContactusAdmin)