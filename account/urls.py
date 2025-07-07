from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user-login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about/', views.about_us, name='about_us'),
    # path('profile/', views.profile, name='profile'),
    # path('edit-profile/', views.edit_profile, name='edit_profile'),
    # path('change-password/', views.change_password, name='change_password'),
    # path('delete-account/', views.delete_account, name='delete_account'),
    # path('activate/<uidb64>/<token>/', views.activate_account, name='activate_account'),
    # path('password-reset/', views.password_reset_request, name='password_reset'),
    # path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('password-reset-complete/', views.password_reset_complete, name='password_reset_complete'),
    # path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
    # path('email-verification/', views.email_verification, name='email_verification'),
    # path('email-verification-resend/', views.email_verification_resend, name='email_verification_resend'),
    # path('email-verification-success/', views.email_verification_success, name='email_verification_success'),
    # path('email-verification-failure/', views.email_verification_failure, name='email_verification_failure'),
    # path('email-verification-pending/', views.email_verification_pending, name='email_verification_pending'),
]
