from django.contrib import admin
from .models import AcardionSlider

class AcardionSliderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title1',
        'title2',
        'title3',
        'photo',
        'is_published'
    )
    list_display_links = (
        'id',
        'title1',
        'title2',
        'title3',
    )
    list_editable = ('is_published',)


admin.site.register(AcardionSlider,AcardionSliderAdmin)
