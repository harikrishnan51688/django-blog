from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.articles, name='blogs'),
    path('article/<str:pk>/', views.singlearticle, name='article'),
    path('article-form/', views.createarticle, name='createarticle'),
    # path('commentarticle/', views.commentarticle, name='comment'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)