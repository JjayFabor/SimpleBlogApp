from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from .serializer import PostSerializer
from .forms import *
from .models import *


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
    comment = post.comments.all()
    likes = post.likes.count()
    user_has_liked = post.likes.filter(user=request.user).exists()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("posts:post-detail", pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "main_post.html",
        {
            "post": post,
            "comments": comment,
            "comment_form": comment_form,
            "likes": likes,
            "user_has_liked": user_has_liked,
        },
    )


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect("posts:post-detail", pk=post.pk)
