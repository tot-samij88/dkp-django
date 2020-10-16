from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'sub_text',
        'is_published'
    )
    list_display_links = (
        'id',
        'title',
        'sub_text',
    )
    list_editable = ('is_published',)

admin.site.register(About,AboutAdmin)