from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),

    path('', views.loginuser),
    path('profile/<str:pk>/', views.profile, name='profile'),

    path('edit-profile/', views.editprofile, name='edit-profile'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password_initial.html'), name='reset_password_initial'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete'),

    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    # path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_done.html'), name='password_change_done')
]