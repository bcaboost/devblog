from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Subscriber
from .forms import (
    CommentForm,
    SignUpForm,
    CretePostForm,
    UpdateForm
)


def homepage(request):
    if 'search' in request.GET:
        term = request.GET.get('search')
        post_list = Blog.objects.filter(published=True).filter(title__icontains=term).order_by('-created_on')
    else:
        post_list = Blog.objects.filter(published=True).order_by('-created_on')
    paginator = Paginator(post_list, 15)
    page_number = request.GET.get('page', 1)
    post = paginator.get_page(page_number)
    return render(request, 'index.html', {'posts' : post})


def single_post(request, author, slug):
    blog = get_object_or_404(Blog, published=True, slug=slug, author__username=author)
    blog.views += 1
    blog.save()
    comments = blog.comments.filter(active=True).order_by('-created_on')
    comment_form = CommentForm(request.POST or None)
    new_comment = None
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = blog
        new_comment.save()
    return render(request, 'post.html', {'post': blog, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


def author_page(request, author):
    author = get_object_or_404(User, username=author, is_active=True)
    if 'search' in request.GET:
        term = request.GET.get('search')
        post_list = Blog.objects.filter(published=True, author=author).filter(title__icontains=term).order_by('-created_on')
    else:
        post_list = Blog.objects.filter(published=True, author=author).order_by('-created_on')
    paginator = Paginator(post_list, 15)
    page_number = request.GET.get('page', 1)
    post = paginator.get_page(page_number)
    return render(request, 'index.html', {'posts' : post, 'author' : author.first_name + ' ' + author.last_name})


def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'forms.html', {'form': form})


@login_required()
def create_post(request):
    if request.method == 'POST':
        form = CretePostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = CretePostForm()
    return render(request, 'forms.html', {'form': form})


@login_required()
def update_post(request, slug):
    instance = get_object_or_404(Blog, slug=slug)
    form = CretePostForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'forms.html', {'form' : form, 'slug' : slug})


@login_required()
def delete_post(request):
    if request.method == 'POST':
        data = get_object_or_404(Blog, slug=request.POST.get('slug'), author=request.user)
        data.delete()
        return redirect('dashboard')
    else:
        raise Http404()


@login_required()
def user_change(request):
    instance = get_object_or_404(User, username=request.user.username, is_active=True)
    form = UpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'forms.html', {'form' : form})


@login_required()
def dashboard(request):
    if 'search' in request.GET:
        term = request.GET.get('search')
        post_list = Blog.objects.filter(author=request.user).filter(title__icontains=term).order_by('-created_on')
    else:
        post_list = Blog.objects.filter(author=request.user).order_by('-created_on')
    paginator = Paginator(post_list, 15)
    page_number = request.GET.get('page', 1)
    post = paginator.get_page(page_number)
    return render(request, 'index.html', {'posts' : post})


def subscribe(request):
    email = request.POST.get('email')
    if email:
        obj = Subscriber(email=email)
        obj.save()
    return redirect('homepage')