from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path("", views.employee_list_view, name='employee_list'),
    path("<field>/<op>/<val>", views.employee_list_view,
         name='employee_list_filtered'),
    path('<int:pk>', views.EmployeeDetailView.as_view(), name='emp_details'),
    path('add', views.EmployeeCreateView.as_view(), name='emp_create')
]
