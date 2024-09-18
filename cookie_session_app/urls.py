from django.urls import path
from . import views

app_name = 'cookie_session_app'
urlpatterns = [
    path("", views.index, name='index'),
    path("explore", views.explore, name='explore')
]
