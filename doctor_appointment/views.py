from django.shortcuts import render
from doctor_appointment.models import Doctors, Appointments
from rest_framework import viewsets
from .serializers import DoctorSerializer, AppointmentSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer
# Create your views here.
