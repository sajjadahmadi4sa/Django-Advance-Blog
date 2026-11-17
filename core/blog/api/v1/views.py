# from rest_framework.decorators import  permission_classes, action
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)

# from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category

# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination

# example for @api_view and @permission_classes

# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response (serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# example for ListCreateAPIView

# class PostList(ListCreateAPIView):
#     # getting a list of posts and create a post
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)


# @api_view(["GET","PUT","DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postDetail(request, id):
#     post = get_object_or_404(Post,pk=id,status=True)
#     if request.method == "GET" :
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT" :
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE" :
#         post.delete()
#         return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)


# example for RetrieveUpdateDestroyAPIView

# class PostDetail (RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)


# example for viewsets


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact", "in"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
