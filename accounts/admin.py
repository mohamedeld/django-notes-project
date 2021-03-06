from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','slug','headline','join_date']
    list_filter = ['headline','join_date']
    search_fields = ['user__first_name','headline','bio']
    list_editable = ['headline']
    list_display_links = None

admin.site.register(Profile,ProfileAdmin)
