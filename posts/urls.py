from django.urls import path, include
from .views import *

app_name = "posts"

urlpatterns = [
    path("", PostView.as_view()),
    path("createpost/", create_post, name="create-post"),
    path('post/<int:pk>/', postDetails, name='post-detail'),
    path("myposts/", myPosts, name="my-posts"),
]
