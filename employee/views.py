from django.shortcuts import render
from typing import Any
from django.http import HttpResponse
from django.db.models import Q
from .models import Employee
from .forms import EmployeeForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/emp_details.html'


class EmployeeCreateView(CreateView):
    form_class = EmployeeForm

    def get_success_url(self) -> str:
        return reverse('employee:emp_details', args=[self.object.id])


def employee_list_view(request, field=None, op=None, val=None):
    context = {}
    context['emp_form'] = EmployeeForm()

    if field is None:
        context['employee_list'] = Employee.objects.all()
        return render(request, 'employee/index.html', context)

    if field not in ['name', 'age', 'address']:
        context['error'] = f'Invalid field: {field}; use name, age or address'
        context['employee_list'] = Employee.objects.all()
        return render(request, 'employee/index.html', context)

    if op not in ['startswith', 'contains', 'lte']:
        context['error'] = f'Invalid op: {op}, use startswith, contains or lte'
        context['employee_list'] = Employee.objects.all()
        return render(request, 'employee/index.html', context)

    lookup = None
    if op == 'startswith':
        if field == 'name':
            lookup = {'fname__startswith': val}
        elif field == 'address':
            lookup = {'address__startswith': val}
    elif op == 'contains':
        if field == 'name':
            lookup = [Q(fname__icontains=val), Q(lname__icontains=val)]
        elif field == 'address':
            lookup = {'address__icontains': val}
    else:
        try:
            if field == 'age':
                lookup = {'age__lte': int(val)}
        except:
            context['error'] = f'{val} is not a number'
            context['employee_list'] = Employee.objects.all()
            return render(request, 'employee/index.html', context)

    if lookup is None:
        context['error'] = f'field: {field} does not support op: {op}'
        context['employee_list'] = Employee.objects.all()
    elif isinstance(lookup, list):
        q_object = Q()
        for q in lookup:
            q_object |= q
        context['employee_list'] = Employee.objects.filter(q_object)
    else:
        context['employee_list'] = Employee.objects.filter(**lookup)

    return render(request, 'employee/index.html', context)
