from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display =('image_tag','title','description', 'url', 'add_date')
    search_fields=('title',)
    list_filter=('title',)
    list_per_page=2

class PostAdmin(admin.ModelAdmin):
    list_display=('image_tag1','post_id','title','content','url',)
    search_fields=('title',)
    list_filter=('cat',)
    class Media:
       js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','static/js/script.js')




admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)