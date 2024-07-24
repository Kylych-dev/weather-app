from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent',
        'url',
        'named_url'
    )
    search_fields = ('name',)


admin.site.register(Menu, MenuAdmin)
