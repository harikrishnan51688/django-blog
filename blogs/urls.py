from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# ckeditor url for upload image
from ckeditor_uploader import views as ckeditor_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.articles, name='blogs'),
    path('article/<str:pk>/', views.singlearticle, name='article'),
    path('article-form/', views.createarticle, name='createarticle'),
    path('edit-or-delete-posts/', views.edit_or_delete_posts, name='edit-or-delete-posts'),
    path('edit-post/<str:pk>/', views.edit_post, name='edit-post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete-post'),

    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', (login_required(ckeditor_views.browse)), name='ckeditor_browse'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)