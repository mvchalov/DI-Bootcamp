from rest_framework import mixins
from .models import Student
from .serializers import StudentSerializer
from django_filters import rest_framework as filters

class StudentOperationsMixin(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    filterset_fields = ['date_joined']


