from django.contrib import admin
from webapp.models import Guest


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'text', 'created_at', 'updated_at', 'status']
    list_filter = ['author']
    search_fields = ['title', 'text']
    fields = ['author', 'email', 'text', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at']



admin.site.register(Guest, GuestBookAdmin)