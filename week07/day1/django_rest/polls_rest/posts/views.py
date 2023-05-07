from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    AllowAny
)
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


class PostView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                instance = Post.objects.get(id=pk)
                serializer = PostSerializer(instance)
            except Post.DoesNotExist:
                return Response({'Detail': 'Post not found'}, status=HTTP_400_BAD_REQUEST)
        else:
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                post = Post.objects.get(id=pk)
                post.delete()
            except Post.DoesNotExist:
                return Response({'Detail': 'Post is not found'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'Detail': 'There is no post to delete'}, status=HTTP_400_BAD_REQUEST)

        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response({'Detail': 'Post is not found'}, status=HTTP_400_BAD_REQUEST)

        except Post.DoesNotExist:
            return Response({'Detail': 'Post is not found'}, status=HTTP_400_BAD_REQUEST)
