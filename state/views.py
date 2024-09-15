from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import State
from .forms import StateDetailsForm
from django.urls import reverse_lazy, reverse


class IndexView(ListView):
    model = State
    template_name = 'state/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        state_form = StateDetailsForm()
        context['state_form'] = state_form
        return context


class StateCreateView(CreateView):
    form_class = StateDetailsForm

    def get_success_url(self) -> str:
        return reverse('state:state_details', args=[self.object.id])


class StateDetailsView(DetailView):
    model = State
    template_name = 'state/state_details.html'


class StateDetailsUpdateView(UpdateView):
    model = State
    form_class = StateDetailsForm
    template_name = 'state/state_details_update.html'

    def get_success_url(self) -> str:
        return reverse('state:state_details', args=[self.object.id])


class StateDetailsDeleteView(DeleteView):
    model = State
    success_url = reverse_lazy('state:index')
