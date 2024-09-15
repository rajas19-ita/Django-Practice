from django.db import models


class State(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    capital = models.CharField(max_length=150, blank=False, null=False)
    language = models.CharField(max_length=100, blank=False, null=False)
    population = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return f"""{self.name}\ncapital    : {self.capital}\nlanguage   : {self.language}\npopulation : {self.population}"""
