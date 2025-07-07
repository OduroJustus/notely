from django.contrib import admin
from . models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the CustomUser model.
    """
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'last_login','is_writer')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('first_name',)
    list_per_page = 20
    filter_horizontal = ()
    readonly_fields = ()


    def get_readonly_fields(self, request, obj=None):
        """
        Make the email field read-only in the admin interface.
        """
        if obj:
            return ('email','first_name', 'last_name',)
        return super().get_readonly_fields(request, obj)
