from django.contrib import admin

from .models import FirstSlide
from .models import NextSlide


class FirstSlideAdmin(admin.ModelAdmin):
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


class NextSlideAdmin(admin.ModelAdmin):
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


admin.site.register(FirstSlide, FirstSlideAdmin)
admin.site.register(NextSlide, NextSlideAdmin)
