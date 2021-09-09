from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'subject']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    filter_horizontal = ()
    fieldsets = (
        (None,
         {'fields': ('name', 'email', 'phone_number')}),
        ('Message', {'fields': ('message',)}),
    )

