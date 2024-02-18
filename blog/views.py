from django.shortcuts import render
from .models import Post
from django.http import Http404 
from django.shortcuts import get_object_or_404

# Create your views here.

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.xhtml', {'post': post})



def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.xhtml', {'posts': posts})

