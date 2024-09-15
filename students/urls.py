from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    path('add', views.StudentCreateView.as_view(), name='student_form'),
    path('update/<int:id>', views.update_details, name='student_update'),
    path('delete/<int:pk>', views.DeleteDetailsView.as_view(), name='student_delete')
]
