"""
URL configuration for loans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("bankpartners.urls")),
=======
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("cooperative.urls")),
=======
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('document.urls')),
    
    path('farmerLoan/',include('farmerLoan.urls')),
   
>>>>>>> 0deec2764997999f18229389ea37de61606ba027
>>>>>>> 4f0891618da362996c36835b56698068c12abe0c
]
