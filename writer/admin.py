from django.contrib import admin
from .models import Article, AuditLog, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'description',)
    search_fields = ('name', 'description')
    list_filter = ('user',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_published', 'is_premium', 'created_at', 'updated_at',)
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'is_premium', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    # prepopulated_fields = {'slug': ('title',)}


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "article",
        "field_name",
        "old_value",
        "new_value",
        "timestamp",
    )
    search_fields = (
        "user__fisrt_name",
        "user__last_name",
        "article__title",
        "field_name",
    )
    list_filter = ("timestamp", "field_name")




