from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsAdmin, IsEditor, IsUser

class CustomOrPermission(permissions.BasePermission):
    def __init__(self, *perms):
        self.perms = perms

    def has_permission(self, request, view):
        return any(perm().has_permission(request, view) for perm in self.perms)

    def has_object_permission(self, request, view, obj):
        print("CustomOrPermission - has_object_permission called")
        result = any(perm().has_object_permission(request, view, obj) for perm in self.perms)
        print(f"CustomOrPermission - has_object_permission result: {result}")
        return result

class BlogListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [CustomOrPermission(IsAdmin, IsEditor)]
        return [CustomOrPermission(IsAdmin, IsEditor, IsUser)]


    def get(self, request):
        blogs = Blog.objects.all().order_by('-created_date')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.copy() 
        data['user'] = request.user.id
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailAPIView(APIView):
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [CustomOrPermission(IsAdmin, IsEditor)]
        return [CustomOrPermission(IsAdmin, IsEditor, IsUser)]

    def get_object(self, pk):
        return get_object_or_404(Blog, pk=pk)

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        blog = self.get_object(pk)
        if blog.user != request.user and request.user.role != "admin":
            return Response({"error": "You are not allowed to edit this post"}, status=status.HTTP_403_FORBIDDEN)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        if blog.user != request.user and request.user.role != "admin":
            return Response({"error": "You are not allowed to edit this post"}, status=status.HTTP_403_FORBIDDEN) 
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
