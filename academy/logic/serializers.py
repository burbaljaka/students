from django.db.models import Avg
from rest_framework import serializers

from .models import *


class StudentSerializer(serializers.ModelSerializer):
    accuracy = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = ['id',
                  'full_name',
                  'birth_date',
                  'accuracy']

    def get_accuracy(self, obj):
        acc = obj.mark_set.aggregate(Avg('mark'))
        return acc['mark__avg']

class MarkSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Mark
        fields = ['id', 'student', 'mark']

    def create(self, validated_data):
        print(self.instance.mark)
        if self.instance.mark not in [2,3,4,5]:
            raise serializers.ValidationError('Please set mark in range [2,3,4,5')
        instance = super(MarkSerializer, self).save(validated_data)
        return instance

    def save(self, **kwargs):
        if self.instance.mark not in [2,3,4,5]:
            raise serializers.ValidationError('Please set mark in range [2,3,4,5')
        instance = super(MarkSerializer, self).save(**kwargs)
        return instance
