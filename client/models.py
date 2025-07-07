import uuid
from django.db import models
from account.models import CustomUser

# Create your models here.

class Subscription(models.Model):
    id = (models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),)
    subscriber_name = models.CharField(max_length=100)
    subscription_plan = models.CharField(max_length=100)
    subscription_cost = models.DecimalField(max_digits=10, decimal_places=2)
    paypal_subscription_id = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    user = models.OneToOneField(CustomUser,max_length=10, on_delete=models.CASCADE, related_name='subscriptions')

    def __str__(self):
        return f"{self.subscriber_name} - {self.subscription_plan}"
    
    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
