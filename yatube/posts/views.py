from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Group, Post


# noinspection PyUnresolvedReferences
def index(request):
    # noinspection PyUnresolvedReferences
    posts = Post.objects[:settings.AMOUNT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts[:settings.AMOUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
