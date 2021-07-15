from django.shortcuts import render
from .models import Post

def home(request):
    #posts is now a variable usable in the frontend via DLT
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})
