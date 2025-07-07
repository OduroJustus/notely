from .models import Article, Category, AuditLog
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django_ckeditor_5.widgets import CKEditor5Widget
from account.models import CustomUser

class ArticleForm(ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='extends'))
    class Meta:
        model = Article
        fields = ["title", "content", "category","is_premium", "is_published"]

    def __init__(self, *args, **kwargs):
        # Accept a user argument for logging purposes
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields[ "category"].queryset = Category.objects.all()  # Populate category choices
        self.fields["category"].empty_label = "Select a Category"

    def clean(self):
        """
        Perform cross-field validation.
        """
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        is_premium = cleaned_data.get("is_premium")
        is_published = cleaned_data.get("is_published")

        if not title:
            self.add_error("title", _("Title cannot be empty."))

        if not content:
            self.add_error("content", _("Content cannot be empty."))

        # Business rule: Premium articles must be published
        if is_premium and not is_published:
            self.add_error("is_published", _("Premium articles must be published."))

        return cleaned_data

    def save(self, commit=True):
        """
        Override save to enforce business logic and log edits.
        """
        article = super().save(commit=False)

        # Auto slugify
        if not article.slug:
            article.slug = slugify(article.title)

        # Enforce is_published = True if is_premium
        if article.is_premium:
            article.is_published = True

        is_create = article.pk is None  # Check if this is a new article
        original_article = None
        
        # If this is an update, get the original article before saving
        if not is_create and self.user:
            try:
                original_article = Article.objects.get(pk=article.pk)
            except Article.DoesNotExist:
                original_article = None

        if commit:
            article.save()

        # Only log updates if this is an update (not create) and we have original data
        if not is_create and self.user and original_article:
            for field in self.Meta.fields:
                old_value = getattr(original_article, field, None)
                new_value = getattr(article, field, None)
                if old_value != new_value:
                    AuditLog.objects.create(
                        user=self.user,
                        article=article,
                        field_name=field,
                        old_value=str(old_value) if old_value is not None else None,
                        new_value=str(new_value) if new_value is not None else None,
                    )

        return article


class UpdateUserForm(forms.ModelForm):
    """
    Form to update user profile information.
    """
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email",]
        exclude = ["password1", "password2",]    
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }   
    
# This form is used to create or update articles.
# It includes validation for the title, content, is_premium, and is_published fields.
# The save method is overridden to ensure the article is saved correctly.
# The clean methods ensure that the fields are not empty and meet the required conditions.