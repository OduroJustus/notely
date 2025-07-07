import uuid
from django.db import models
from account.models import CustomUser

# Create your models here.

class Category(models.Model):
    """
    Model representing a Category.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='categories', verbose_name="Author"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']  # Order by name by default

class Article(models.Model):
    """
    Model representing a Article.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField(max_length=50000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name="Publish this article?")
    is_premium = models.BooleanField(default=False, verbose_name="Is premium?")
    is_standard = models.BooleanField(default=False, verbose_name="Is standard?")
    is_free = models.BooleanField(default=True, verbose_name="Is free?")
    last_modified_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="edited_articles",
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='articles', verbose_name="Author")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles', verbose_name="Category"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['title']  # Order by name by default

    

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name="audit_logs"
    )
    article = models.ForeignKey(
        "Article", on_delete=models.CASCADE, related_name="audit_logs"
    )
    field_name = models.CharField(max_length=255)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.user} changed '{self.field_name}' on '{self.article.title}'"