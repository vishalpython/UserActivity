"""AuthPredefineForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from django.urls import include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.UserRegistration.as_view(),name="user"),
    path("accounts/",include('django.contrib.auth.urls')),
    path("home/",TemplateView.as_view(template_name="home.html"),name="home"),
    path('update/<int:pk>',views.ProfileUpdate.as_view(),name="update"),
    path('UserActivity/',csrf_exempt(views.UserActivity.as_view()))
]
