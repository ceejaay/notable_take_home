"""notable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet 
from shiren.views import prices, scrolls
from doctor_appointment.views import doctor_list, doctor, appointment_list, appointment
from django.conf.urls import include
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# router.register(r'shiren', SwordViewSet, basename="shiren")
# router.register(r'doctors', DoctorViewSet, basename="doctor")
# router.register(r'appointments', AppointmentViewSet, basename="appointment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('shiren/', include('rest_framework.urls', namespace='shiren')),
    path('doctors/', doctor_list),
    path('doctors/<int:pk>/', doctor),
    path('appointment/<int:pk>/', appointment),
    path('doctors/<int:pk>/appointments/', appointment_list),
    path('appointments/', include('rest_framework.urls', namespace='appointments')),
    path('shiren/prices', prices),
    path('shiren/scrolls', scrolls)
]
