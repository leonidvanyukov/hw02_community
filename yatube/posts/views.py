from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:settings.AMOUNT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:settings.AMOUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
