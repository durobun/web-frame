from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone 
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts}) 
    #return HttpResponse("Django로 블로그를 만들어 봅시다.blog")

def get_extra1(request):
    return HttpResponse("extra1")

def get_extra2(request):
    return HttpResponse("extra2")