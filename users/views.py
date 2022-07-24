from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile

# Create your views here.
def loginuser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('blogs')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully logged in')
            return redirect(request.GET['next'] if 'next' in request.GET else 'blogs')
        else:
            messages.error(request, 'Username or Password is incorrect')
    context = {"page":page}
    return render(request, 'users/pages-login.html', context)

def logoutuser(request):
    logout(request)
    messages.error(request, 'Logged out')
    return redirect('login')

def registeruser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created')
            login(request, user)
            return redirect('edit-profile')
        else:
            messages.error(request, 'An error occurred!')
        
    context = {"page":page, "form": form}
    return render(request, 'users/pages-login.html', context)


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    count = profile.article_set.all()
    articles = profile.article_set.all().order_by('created')[:5]

    context = {'profile': profile, 'blog_count': len(count), 'articles': articles}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def editprofile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    count = profile.article_set.all()
    articles = profile.article_set.all().order_by('created')[:10]
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            return redirect('blogs')

    context = {'form':form,'profile': profile, 'articles': articles, 'blog_count': len(count)}
    return render(request, 'users/edit-profile.html', context)