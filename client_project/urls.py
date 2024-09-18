from django.urls import path
from . import views

app_name = 'client_project_app'
urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("login", views.UserLoginView.as_view(), name='login'),
    path("logout", views.logout_view, name='logout'),
    path('clients', views.ClientListView.as_view(), name='client_list'),
    path('clients/add', views.ClientRegisterView.as_view(), name='create_client'),
    path('clients/<int:pk>', views.ClientDetailView.as_view(), name='client_details'),
    path('client/update/<int:pk>',
         views.ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>',
         views.ClientDeleteView.as_view(), name='delete_client'),
    path('projects/add', views.ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(),
         name='project_details')
]
