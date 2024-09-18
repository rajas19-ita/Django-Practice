from django.urls import path
from . import views

app_name = 'bootstrap_practice_app'
urlpatterns = [
    path("", views.index, name="index")
]
