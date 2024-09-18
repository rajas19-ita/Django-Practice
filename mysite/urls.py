"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings/', include('greetings.urls')),
    path('students/', include('students.urls')),
    path('state/', include('state.urls')),
    path('employee/', include('employee.urls')),
    path('media/', include('media_app.urls')),
    path('cookie-session-app/', include('cookie_session_app.urls')),
    path('client-project-app/', include('client_project.urls')),
    path('bootstrap-practice-app/', include('bootstrap_practice_app.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('pet-store/', include('pet_store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
