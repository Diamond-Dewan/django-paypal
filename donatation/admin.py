from django.contrib import admin
from .models import Donate


class DonateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount', 'is_donated']
    ordering = ['id']


admin.site.register(Donate, DonateAdmin)
