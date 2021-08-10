from django.contrib import admin
from .models import Note
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_filter = ['active','last_update','tags']
    list_display=['title','active','last_update']
    search_fields = ['title']
    list_editable = ['active']

admin.site.register(Note,NotesAdmin)
