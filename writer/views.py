from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ArticleForm,UpdateUserForm
from .models import Article, AuditLog
from account.models import CustomUser

# Create your views here.

@login_required(login_url='user_login')
def writer_dashboard(request):
    """
    Render the home page for the client.
    """
    return render(request, "writer/dashboard.html")

@login_required(login_url='user_login')
def create_article(request):
    """
    This function handles the creation of a new article by the author.
    If the request method is POST, it processes the form data and saves the article.
    If the request method is GET, it renders the form for creating a new article.
    :param request: The HTTP request object.
    :return: Rendered template with the article creation form or redirects to the author's articles page
    """
    if request.method == "POST":
        form = ArticleForm(request.POST, user=request.user)
        
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # Set the author
            article.save()
            return redirect("author_articles")
    else:
        form = ArticleForm(user=request.user)

    context = {"articleForm": form}
    return render(request, "writer/create_article.html", context)
   
        

@login_required(login_url='user_login')
def author_article(request):
    auth_user = request.user.id
    """    
    This function retrieves all articles created by the logged-in user (author) and displays them.
    If the author has not created any articles, it displays a message indicating that no articles are available.
    :param request: The HTTP request object.
    :return: Rendered template with the author's articles or a message if no articles are found
    """
    # Get the articles created by the author
    # Filter the articles by the author and order them by creation date
    articles = Article.objects.filter(user=auth_user).order_by('-created_at')
    # If the author has not created any articles, display a message
    if not articles:
        return render(request, "writer/my_articles.html", {"message": "You have not created any articles yet."})
    context = {"articles": articles}

    return render(request, "writer/my_articles.html", context)


@login_required(login_url='user_login')
def update_article(request,pk):
    """
    This function allows the author to update their article.
    It retrieves the article by its primary key (pk) and checks if the user is the author of the article.
    If the user is not the author, it returns an error message.
    If the request method is POST, it updates the article with the data from the form.
    If the request method is GET, it renders the form with the article data.
    If the article does not exist, it returns an error message.
    The function returns a rendered template with the form for updating the article.
    If the article is successfully updated, it redirects to the author's articles page.
    """
    article = get_object_or_404(Article, id=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("author_articles")
    else:
        form = ArticleForm(instance=article, user=request.user)

    context = {"updateArticleForm": form}
    return render(request, "writer/update_article.html", context)

# @login_required(login_url='user_login')
# def update_article(request,pk):
#     """
#     This function allows the author to update their article.
#     It retrieves the article by its primary key (pk) and checks if the user is the author of the article.
#     If the user is not the author, it returns an error message.
#     If the request method is POST, it updates the article with the data from the form.
#     If the request method is GET, it renders the form with the article data.
#     If the article does not exist, it returns an error message.
#     The function returns a rendered template with the form for updating the article.
#     If the article is successfully updated, it redirects to the author's articles page.
#     :param request: The HTTP request object.
#     :param pk: The primary key of the article to be updated.
#     :return: A rendered template with the form for updating the article or a redirect to the author's articles page.
#     :raises Article.DoesNotExist: If the article with the given primary key does not exist.
#     :raises PermissionDenied: If the user is not the author of the article.
#     :raises Http404: If the article does not exist.
#     :raises ValueError: If the form data is not valid.
#     :raises Exception: If there is an error while updating the article.
#     :raises Redirect: If the article is successfully updated, it redirects to the author's articles page.
#     """
#     try:
#         article = Article.objects.get(id=pk, user=request.user)
#         if request.method == "POST":
#             form = ArticleForm(request.POST, instance=article)
#             if form.is_valid():
#                 form.save()
#                 return redirect('author_articles')  # Redirect to the dashboard or another page after saving
#         else:
#             form = ArticleForm(instance=article)
#         # If the request is GET, render the form
#         context = {
#             "updateArticleForm": form,
#         }
#         return render(request, "writer/update_article.html", context)
#     except Article.DoesNotExist:
#         return render(
#             request, "writer/read_article.html", {"message": "Article not found."}
#         )


@login_required(login_url='user_login')
def read_article(request, pk):
    """
    Render the read article page for the client.
    """
    try:
        article = Article.objects.get(id=pk)
        context = {
            'article': article,
        }
        return render(request, "writer/read_article.html", context)
    except Article.DoesNotExist:
        return render(request, "writer/read_article.html", {"message": "Article not found."})

@login_required(login_url='user_login')
def delete_article(request, pk):
    """
    Render the delete article page for the client.
    """
    try:
        if request.method == "GET":
            return render(request, "writer/delete_article.html")
        
        # Get the article by primary key (pk) and ensure the user is the author
        if request.method == "POST":
            article = Article.objects.get(id=pk, user=request.user)
            article.delete()
            return redirect('author_articles')
        return render(request, "writer/delete_article.html")
    except Article.DoesNotExist:
        return render(request, "writer/article_not_found.html")
    

@login_required(login_url="user_login")
def article_edited_history(request, pk):
    """
    Show the edit history (audit log) for a specific article.
    """
    article = get_object_or_404(Article, pk=pk)

    # Only allow the author or admin to view
    if request.user != article.user and not request.user.is_staff:
        return render(request,"writer/access_denied.html")

    audit_logs = AuditLog.objects.filter(article=article).order_by("-timestamp")
    context = {"article": article, "audit_logs": audit_logs}
    return render(request, "writer/article_history.html", context)

@login_required(login_url="user_login")
def get_edited_articles_by_writer1(request):
    """
    Show the edit history (audit log) for all articles by the author.
    """
    audit_logs = AuditLog.objects.filter(user=request.user).order_by("-timestamp")
    
    if not audit_logs:
        return render(
            request,
            "writer/article_edited_history.html",
            {"message": "You have not edited any articles."},
        )

    context = {"audit_logs": audit_logs}
    return render(request, "writer/article_edited_history.html", context)

@login_required(login_url="user_login")
def get_edited_articles_by_writer(request):
    """
    This function retrieves all articles that the logged-in user (author) has edited
    and displays them in a template.
    :param request: The HTTP request object.
    :return: Rendered template with the list of edited articles by the user
    """
    articles = Article.objects.filter(audit_logs__user=request.user).distinct()
    context = {
        "edited_articles": articles
    }
    return render(request, "writer/get_edited_articles_by_writer.html", context)

@login_required(login_url="user_login")
def publish_unpublish_article(request, pk):
    """
    This function allows the author to publish or unpublish an article.
    If the user is not the author or an admin, it denies access.
    :param request: The HTTP request object.
    :param pk: The primary key of the article to be toggled.
    :return: Redirects to the author's articles page after toggling the publish status
    """
    article = get_object_or_404(Article, pk=pk)

    # Only allow the author or admin to publish
    if request.user != article.user and not request.user.is_staff:
        return render(request, "writer/access_denied.html")
    
    # If the article is not published, publish it
    article.is_published = not article.is_published
    article.save()
    
    return redirect("author_articles")

@login_required(login_url="user_login")
def set_unset_premium_article(request, pk):
    """
    This function allows the author to set or unset the premium status of an article.
    If the user is not the author or an admin, it denies access.
    :param request: The HTTP request object.
    :param pk: The primary key of the article to be toggled.
    :return: Redirects to the author's articles page after toggling the premium status
    """
    article = get_object_or_404(Article, pk=pk)

    # Deny access if the user is neither the author nor an admin
    if request.user != article.user and not request.user.is_staff:
        return render(request, "writer/access_denied.html")

    # Toggle premium status for the article
    article.is_premium = not article.is_premium
    article.save()

    return redirect("author_articles")


@login_required(login_url="user_login")
def account_management(request):
    """
    This function allows the user to update their account information.
    If the request method is POST, it processes the form data and updates the user's information.
    If the request method is GET, it renders the form with the user's current information.
    :param request: The HTTP request object.
    :return: Rendered template with the form for updating user information or redirects to the author's articles page
    """
    form = UpdateUserForm(instance=request.user)
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("author_articles")
    context = { "updateUserForm": form,}
    return render(request, "writer/account_management.html", context)


@login_required(login_url="user_login")
def delete_account(request):
    """
    This function allows the user to delete their account.
    If the request method is POST, it deletes the user's account and redirects to the login page.
    If the request method is GET, it renders the delete account confirmation page.
    :param request: The HTTP request object.
    :return: Rendered template for account deletion confirmation or redirects to the login page after deletion
    """
    if request.method == "POST":
        user = CustomUser.objects.get(email=request.user)
        # Delete the user account
        user.delete()
        return redirect("user_login")
    
    return render(request, "writer/delete_account.html")