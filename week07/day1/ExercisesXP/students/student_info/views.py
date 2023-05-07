from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


class StudentView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                instance = Student.objects.get(id=pk)
                serializer = StudentSerializer(instance)
            except Student.DoesNotExist:
                return Response({'Detail': 'This student does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                item = Student.objects.get(id=pk)
                item.delete()
            except item.DoesNotExist:
                return Response({'Detail': 'Student is not found'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'Detail': 'Cannot delete many students'}, status=HTTP_400_BAD_REQUEST)

        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            item = Student.objects.get(id=pk)
            serializer = StudentSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            else:
                return Response({'Detail': 'Student is not found'}, status=HTTP_400_BAD_REQUEST)

        except item.DoesNotExist:
            return Response({'Detail': 'Student is not found'}, status=HTTP_400_BAD_REQUEST)
