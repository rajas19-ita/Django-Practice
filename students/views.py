from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import StudentForm
from .models import Student
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
import json


class StudentCreateView(CreateView):
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')


class StudentListView(ListView):
    model = Student
    template_name = 'students/index.html'


@csrf_exempt
def update_details(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        student1 = Student.objects.get(id=id)
        student1.student_name = data['student_name']
        student1.email = data['email']
        student1.age = int(data['age'])
        student1.save()
        return JsonResponse(data={'success': True})


class DeleteDetailsView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')
