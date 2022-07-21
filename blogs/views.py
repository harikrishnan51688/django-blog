import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.template import context

from users.models import Profile
from .models import Article, Comment
from .forms import Articleform, CommentForm, EditArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Main page all blog posts
def articles(request):
    blogs = Article.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/main-blog.html', context)

# View for individual article and comment form
def singlearticle(request, pk):
    blog = Article.objects.get(id=pk)
    tags = blog.tags.all()
    length_tags = len(tags)
    owner = blog.owner.username
    profile = Profile.objects.get(username=owner)
    blog.getcommentcount
    
    form = CommentForm()
    if request.method == 'POST':
       # print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = blog
            comment.owner = request.user.profile
            comment.save()
            blog.getcommentcount
            return redirect('article', pk=blog.id)

    length_articles = len(profile.article_set.all())

    context = {'blog': blog, 'tags': tags, 'length_tags': length_tags, 'length_articles': length_articles, 'profile': profile, 'commentform': form}
    return render(request, 'blogs/blog-single.html', context)

# View for creating article
@login_required(login_url='login')
def createarticle(request):
    form = Articleform()
    profile = request.user.profile

    if request.method == 'POST':
        print(request.POST)
        form = Articleform(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = profile
            article.save()

            return redirect('blogs')

    context = {'form': form}
    return render(request, 'blogs/article_form.html', context)

# Main page for all post for edit and delete
@login_required(login_url='login')
def edit_or_delete_posts(request):
    profile = request.user.profile
    articles = profile.article_set.all()
    context = {'articles': articles}
    return render(request, 'blogs/edit-or-delete-posts.html', context)

# Individual page for edit blog post
@login_required(login_url='login')
def edit_post(request, pk):
    blog = Article.objects.get(id=pk)
    form = EditArticleForm(instance=blog)
    if request.method == "POST":
        form = EditArticleForm(request.POST, request.FILES, instance=blog)
        if form.is_valid:
            form.save()
            return redirect('edit-or-delete-posts')
    context = {"form": form}
    return render(request, 'blogs/edit-post.html', context)

# View for delete blog post
@login_required(login_url='login')
def delete_post(request, pk):
    blog = Article.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('edit-or-delete-posts')
    return render(request, 'blogs/delete-post.html')