"""
URL configuration for QuantumQuick project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from verdevalvet.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', index, name='index'),
=======
    path('', home, name='home'),
>>>>>>> 977f1b8c4a8f8bdf8c0eb3fb9665ed1a54b0c7ba
    path('checkout/', checkout, name='checkout'),
    path('feedback/', feedback, name='feedback'),
    path('ticket/', my_ticket, name='my_ticket'),
    path('contact/', contact, name='contact'),
    # rute untuk event 
    path('events/', events, name='events')
]
