from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ObjectDoesNotExist
from rest_framework.serializers import ValidationError

from .serializers import *


class MarkViewset(ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

    def create(self, request, *args, **kwargs):

        try:
            user = Student.objects.get(pk=request.data.pop('student'))
        except (KeyError, ObjectDoesNotExist):
            raise ValidationError('Cannot find such student')
        if request.data['mark'] not in [2,3,4,5]:
            raise ValidationError('Cannot set such mark. Please choose in between 2-5')
        serializer = MarkSerializer(data=request.data)
        serializer.is_valid()
        new_mark = Mark.objects.create(**serializer.validated_data, student=user)
        new_mark.save()
        return Response(MarkSerializer(new_mark).data)


class StudentViewset(ModelViewSet):
    queryset = Student.objects.all().prefetch_related()
    serializer_class = StudentSerializer
