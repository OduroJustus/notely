from django.contrib import admin
from .models import Subscription

# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber_name', 'subscription_plan', 'subscription_cost', 'start_date', 'end_date', 'is_active', 'user')
    search_fields = ('subscriber_name', 'subscription_plan')
    list_filter = ('is_active', 'start_date', 'end_date')
    ordering = ('-start_date',)
    list_per_page = 20

   