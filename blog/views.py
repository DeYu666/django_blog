from django.shortcuts import render
from .models import Post, TopCate, Category
from django.shortcuts import get_object_or_404
import markdown

# Create your views here.

from django.http import HttpResponse


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})


def memory(request, pk):
    # cate = get_object_or_404(Category, topcate=pk)
    cate = Category.objects.filter(topcate=pk)
    return render(request, 'blog/memory.html', context={'category': cate})


def cate_list(request, pk):
    posts = Post.objects.filter(category=pk)
    return render(request, 'blog/content_list.html', context={'posts': posts})