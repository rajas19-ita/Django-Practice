from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.student_name}'
