from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("cbv_index", views.IndexView.as_view(), name="cbv_index"),
    path("post/", views.PostListView.as_view(), name="post_list"),
    path("post/api/", views.PostListApiView.as_view(), name="post_list_view"),
    path("post<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path(
        "post<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post_delete",
    ),
    path("api/v1/", include("blog.api.v1.urls", namespace="api_v1")),
]
