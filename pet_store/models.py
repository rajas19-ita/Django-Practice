from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    breed = models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField(default=0.00, blank=False, null=False)

    def __str__(self) -> str:
        return f'name: {self.name}\nbreed: {self.breed}\nprice:{self.price}'
