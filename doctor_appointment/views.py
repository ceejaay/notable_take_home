from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from doctor_appointment.models import Doctors, Appointments
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .serializers import DoctorSerializer, AppointmentSerializer



def validate_time(value):
    if not value:
        raise serializers.ValidationError("Time isn't right")
    return value





@csrf_exempt
def doctor_list(request):
    if request.method == 'GET':
        docs = Doctors.objects.all()
        serializer = DoctorSerializer(docs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def doctor(request, pk):
    try:
        doc = Doctors.objects.get(pk=pk)
    except Doctors.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        doc_data = DoctorSerializer(doc)
        print("serializer data", doc_data)
        return JsonResponse(doc_data.data)
    elif request.method == 'DELETE':
        doc.delete()
        return HttpResponse(status=204)

@csrf_exempt
def appointment(request, pk):
    try:
        appt = Appointments.objects.get(pk=pk)
    except Appointments.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        appt_data = AppointmentSerializer(appt)
        d = appt_data.data['date_time']
        correct_time(d)
        return JsonResponse(appt_data.data)
    elif request.method == 'DELETE':
        appt.delete()
        return HttpResponse(status=204) 



@csrf_exempt
def appointment_list(request, pk):
    appts = Appointments.objects.filter(doctor_id=pk)
    if request.method =='GET':
            appt_list = AppointmentSerializer(appts, many=True)
            return JsonResponse(appt_list.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(doctor_id=pk)
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)




# class AppointmentViewSet(viewsets.ModelViewSet):
#     queryset = Appointments.objects.all()
#     serializer_class = AppointmentSerializer
# Create your views here.
