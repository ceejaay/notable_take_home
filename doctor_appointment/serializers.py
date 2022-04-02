from doctor_appointment.models import Doctors, Appointments
from rest_framework import serializers

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctors
        fields = ['first_name', 'last_name', 'unique_id']
    

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Appointments
        fields = ['patient_first_name', 'patient_last_name', 'date_time', 'appt_type', 'unique_id']

    def validate(self, data):
        if data['date_time'].minute not in [15, 30, 45, 00]:
            raise serializers.ValidationError("Time must be at 15 min")
        return data


