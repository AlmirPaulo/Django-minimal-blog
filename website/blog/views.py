from django.shortcuts import render, redirect
from .models import Post, CommentForm

def home(request):
    #posts is now a variable usable in the frontend via DLT
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})

def post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post', slug=post.slug)
    else:
        form = CommentForm()

    return render(request,'blog/post.html', {'post':post, 'form':form})


