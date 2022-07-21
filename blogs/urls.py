from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.articles, name='blogs'),
    path('article/<str:pk>/', views.singlearticle, name='article'),
    path('article-form/', views.createarticle, name='createarticle'),
    path('edit-or-delete-posts/', views.edit_or_delete_posts, name='edit-or-delete-posts'),
    path('edit-post/<str:pk>/', views.edit_post, name='edit-post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete-post'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)