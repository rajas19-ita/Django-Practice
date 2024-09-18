from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Pet


class IndexPageView(TemplateView):
    template_name = 'pet_store/index.html'


class ServicePageView(TemplateView):
    template_name = 'pet_store/service.html'


class PetsListFiltered(ListView):
    template_name = 'pet_store/pet_list_page.html'

    def get_queryset(self) -> QuerySet[Any]:
        return Pet.objects.filter(price__gt=5000)
