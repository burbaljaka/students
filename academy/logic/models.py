from django.db import models
from rest_framework.response import Response
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.IntegerField(validators=[MinValueValidator(2),
                               MaxValueValidator(5)])

    def __str__(self):
        return str(self.mark) + ' ' + self.student.full_name