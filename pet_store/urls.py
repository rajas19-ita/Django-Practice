from django.urls import path
from . import views

app_name = 'pet_store'
urlpatterns = [
    path("", views.IndexPageView.as_view(), name='index'),
    path("service", views.ServicePageView.as_view(), name="service_page"),
    path("gt", views.PetsListFiltered.as_view(), name='price_gt_5000')
]
