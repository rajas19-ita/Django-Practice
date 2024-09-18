from django.db import models


class Employee(models.Model):
    fname = models.CharField(max_length=100, blank=False, null=False)
    lname = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    profile_image = models.ImageField(
        upload_to='emp_profile_img', default='', null=False)

    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'
