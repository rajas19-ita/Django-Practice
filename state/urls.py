from django.urls import path
from . import views

app_name = "state"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.StateDetailsView.as_view(), name="state_details"),
    path("add", views.StateCreateView.as_view(), name="state_add"),
    path("update/<int:pk>", views.StateDetailsUpdateView.as_view(),
         name="state_update"),
    path("delete/<int:pk>", views.StateDetailsDeleteView.as_view(), name='state_delete')
]
