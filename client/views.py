from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from writer.models import Article
from . models import Subscription


# Create your views here.
@login_required(login_url="user_login")
def client_dashboard(request):
    """
    Render the home page for the client.
    """
    return render(request, "client/dashboard.html")

@login_required(login_url="user_login")
def subscribed_articles(request):
    """
    Render the profile page for the client.
    Show free articles if no active subscription exists.
    """
    user_subscription = Subscription.objects.filter(
        is_active=True, user=request.user
    ).first()
    print(user_subscription)

    if user_subscription:
        user_subscription_plan = user_subscription.subscription_plan

        if user_subscription_plan == "Standard":
            articles = Article.objects.filter(is_published=True, is_standard=True)
        elif user_subscription_plan == "Premium":
            articles = Article.objects.filter(is_published=True)
        else:
            articles = Article.objects.filter(is_published=True, is_free=True)
    else:
        # No subscription: show free articles only
        user_subscription_plan = "Free"
        articles = Article.objects.filter(is_published=True, is_free=True)

    context = {
        "clientArticles": articles,
        "user_subscription_plan": user_subscription_plan,
    }

    return render(request, "client/subscribed_articles.html", context)
