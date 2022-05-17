from django.shortcuts import render, get_object_or_404
from .models import Post, Group

# Create your views here.


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'titles': text,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'titles': text,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
