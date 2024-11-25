from django.contrib import admin
from app.domain.models import Paste


@admin.register(Paste)
class PasteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_private', 'created_at', 'unique_url')
    list_filter = ('is_private', 'created_at')
    search_fields = ('title', 'owner__username', 'content')
    readonly_fields = ('unique_url', 'created_at')

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff
