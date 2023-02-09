from django.contrib import admin
from .models import Contact

def mark_as_read(modeladmin, request, queryset):
    queryset.update(is_read=True)
mark_as_read.short_description = "Oznacz jako przeczytane"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    actions = [mark_as_read]

admin.site.register(Contact, ContactAdmin)