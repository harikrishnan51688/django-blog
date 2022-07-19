import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.template import context

from users.models import Profile
from .models import Article, Comment
from .forms import Articleform, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def articles(request):
    blogs = Article.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/main-blog.html', context)


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

# @login_required(login_url='login')
# def commentarticle(request, pk):
#     blog = Article.objects.get(id=pk)
#     form = CommentForm()
#     if request.method == 'POST':
#         print(request.POST)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context = {'commentform': form, 'blog': blog}

#     return render('blogs/blog-single.html', context)
