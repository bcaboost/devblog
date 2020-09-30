from django.shortcuts import render, get_object_or_404

from .models import APIUserDoc, APIPostDoc


def developer_index(request):
    post = get_object_or_404(APIPostDoc, published=False, slug='main-page')
    return render(request, 'api/post.html', {'post' : post})


def post_api_doc(request, slug):
    post = get_object_or_404(APIPostDoc, published=True, slug=slug)
    return render(request, 'api/post.html', {'post' : post})


def user_api_doc(request, slug):
    post = get_object_or_404(APIUserDoc, published=True, slug=slug)
    return render(request, 'api/post.html', {'post' : post})

def post_api_index(request):
    post = get_object_or_404(APIPostDoc, published=False, slug='homepage')
    return render(request, 'api/post.html', {'post' : post})

def user_api_index(request):
    post = get_object_or_404(APIUserDoc, published=False, slug='homepage')
    return render(request, 'api/post.html', {'post' : post})