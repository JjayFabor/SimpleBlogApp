from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from .serializer import PostSerializer
from .forms import PostForm


class PostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@login_required
def myPosts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "posts_list.html", {"posts": posts, "show_header": True})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return redirect("posts:my-posts")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form, "show_header": True})


def postDetails(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "main_post.html", {"post": post})
