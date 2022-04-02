from django.db import models
import uuid

# Create your models here.

class Doctors(models.Model):
    first_name  = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str_(self):
        return f"{first_name} {last_name}"



class Appointments(models.Model):
    APPT_TYPE = (
            ('N', 'New Patient'), 
            ('R', "Returning Patient")
            )
    patient_first_name = models.CharField(max_length=256)
    patient_last_name = models.CharField(max_length=256)
    date_time = models.DateTimeField()
    appt_type = models.CharField(max_length=1, choices=APPT_TYPE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    #relations
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)

    # def __str_(self):
    #     return f"{patient_first_name} {patient_last_name}, {date_time}"


