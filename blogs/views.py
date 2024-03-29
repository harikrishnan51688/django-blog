import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.template import context

from users.models import Profile
from .models import Article, Comment
from .forms import Articleform, CommentForm, EditArticleForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Main page all blog posts
def articles(request):
    blogs = Article.objects.all()

    # pagination for main blog page
    page = request.GET.get('page', 1)

    paginator = Paginator(blogs, 6) # 6 posts per page

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {'page_obj': page_obj}
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
        if form.is_valid:
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

    # pagination for edit or delete page
    page = request.GET.get('page', 1)

    paginator = Paginator(articles, 6) # 6 post per page


    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {'page_obj': page_obj}
    return render(request, 'blogs/edit-or-delete-posts.html', context)

# Individual page for edit blog post
@login_required(login_url='login')
def edit_post(request, pk):
    profile = request.user.profile
    blog = profile.article_set.get(id=pk)
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
    profile = request.user.profile
    blog = profile.article_set.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('edit-or-delete-posts')
    return render(request, 'blogs/delete-post.html')

# View for delete comment 
@login_required(login_url='login')
def delete_comment(request, pk):
    profile = request.user.profile
    comment = profile.comment_set.get(id=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect(request.GET['next'] if 'next' in request.GET else 'blogs')
    return render(request, 'blogs/delete-comment.html')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)