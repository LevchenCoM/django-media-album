from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Media._meta.fields]
    list_display_links = ['title', 'description', 'id']

    class Meta:
        model = Media
