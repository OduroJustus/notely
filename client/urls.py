from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.client_dashboard, name="client_dashboard"),
    path("subscribed-articles/", views.subscribed_articles, name="subscribed_articles"),
]
