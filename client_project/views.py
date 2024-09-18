from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ClientForm, ProjectForm
from .models import Client, Project
from django.contrib.auth.models import User


class UserLoginView(LoginView):
    template_name = 'client_project/login.html'
    next_page = reverse_lazy('client_project_app:index')


class IndexView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'client_project/index.html'
    login_url = reverse_lazy('client_project_app:login')

    def get_queryset(self):
        return self.request.user.project_set.all()


class ClientRegisterView(LoginRequiredMixin, CreateView):
    form_class = ClientForm
    template_name = 'client_project/client_register_form.html'
    login_url = reverse_lazy('client_project_app:login')

    def get_success_url(self) -> str:
        return reverse_lazy('client_project_app:client_details', args=[self.object.id])


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_project/client_list.html'
    login_url = reverse_lazy('client_project_app:login')


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_project/client_detail_page.html'
    login_url = reverse_lazy('client_project_app:login')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_project/client_update_page.html'
    login_url = reverse_lazy('client_project_app:login')

    def get_success_url(self) -> str:
        return reverse_lazy('client_project_app:client_details', args=[self.object.id])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client_project_app:client_list')
    login_url = reverse_lazy('client_project_app:login')


class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'client_project/project_create_page.html'
    login_url = reverse_lazy('client_project_app:login')
    success_url = reverse_lazy('client_project_app:index')


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'client_project/project_detail_page.html'
    login_url = reverse_lazy('client_project_app:login')


def logout_view(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        return HttpResponse('Logged out successfully!')
    return HttpResponseRedirect(reverse('client_project_app:login'))
