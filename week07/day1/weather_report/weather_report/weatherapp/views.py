from django.shortcuts import render
from .models import Report
from .serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListCreateAPIView


class ReportMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Create your views here.
# class ReportView(APIView):
#
#     permission_classes = (AllowAny, )
#
#     def get(self, request, *args, **kwargs):
#         queryset = Report.objects.all()
#         serializer = ReportSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = ReportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)