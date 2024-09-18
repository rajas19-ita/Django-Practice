from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.name}\n{self.email}\n{self.address}'


class Project(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=False, blank=False, related_name='projects')
    users = models.ManyToManyField(User)
