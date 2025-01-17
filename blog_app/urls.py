from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("user.urls", "user")),
    path("posts/", include("posts.urls", "posts")),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
