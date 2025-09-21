from django.shortcuts import render, HttpResponse
from posts.models import Post


def test_view(request):
    return HttpResponse("First view is working")

def html_view(request):
    return render(request, "base.html")

def posts_list_view(request): 
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", context={"posts_list": posts})

def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, "posts/posts_list.html", context={"post": post})