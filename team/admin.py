from django.contrib import admin
from .models import OurTeamate


class OurTeamateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title1',
        'title2',
        'title3',
        'title4',
    )
    list_display_links = (
        'id',
        'title1',
        'title2',
        'title3',
        'title4',
    )


admin.site.register(OurTeamate,OurTeamateAdmin)
