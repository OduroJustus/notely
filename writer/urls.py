from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.writer_dashboard, name="writer_dashboard"),
    path("create/", views.create_article, name="create_article"),
    path("my-articles/", views.author_article, name="author_articles"),
    path("update-articles/<str:pk>/", views.update_article, name="update_article"),
    path("read-articles/<str:pk>/", views.read_article, name="read_article"),
    path("delete-articles/<str:pk>/", views.delete_article, name="delete_article"),
    path(
        "article/edited/<str:pk>/history/",
        views.article_edited_history,
        name="article_edited_history",
    ),
    path(
        "edited-articles/",
        views.get_edited_articles_by_writer,
        name="get_edited_articles_by_writer",
    ),
    path(
        "publish-unpublish/article/<str:pk>/",
        views.publish_unpublish_article,
        name="publish_unpublish_article",
    ),
    path(
        "set-unset/premium/<str:pk>/",
        views.set_unset_premium_article,
        name="set_unset_premium_article",
    ),
    path("account-management/", views.account_management, name="account_management"),
    path("delete-account/", views.delete_account, name="delete_account"),
]
