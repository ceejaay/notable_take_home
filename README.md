# Notable Take-home project April 2, 2022
## By [Chad Jemmett](https://www.linkedin.com/in/chad-jemmett-a3a0a347/)


Description

This backend app provides 4 endpoints to manage a doctor's appointments. A take-home project for Notable. 
This Projects Uses:
* Python
* Django
* Django REST Framework
* SQLite3

### Instructions

Clone the repository on your local machine.

run `pip -r requirements.txt`

`./manage.py makemigrations`
`./manage.py migrate`
`./manage.py runserver`

Navigate to [localhost:8000/doctors/](localhost:8000/doctors/)


### Endpoints
`/doctors/` 
* `GET` - list of all doctors.
* `POST` - Create a doctor resource.
	* Returns the newly created doctor resource.


`/doctors/<pk number>/` 
* `GET` - Returns individual doctor data.
* `DELETE` - Deletes a single doctor.
	* Returns the number of doctors deleted.


`/doctors/<pk number>/appointments/`  

* `GET` - Returns a list of appointments for an individual doctor.
* `POST`- Create a new appointment connected to the doctor.
	* Returns newly created appointment.

`daily-appointments/<doctor's pk number>?date=yyyy-mm-dd`
* `GET` - Returns a list of appointments by doctor and a specific day.




### Data formats

Doctor Data
```
{
 "first_name": "first name",
 "last_name": "last name"
}

```
Appointment Data
```
{
  "patient_first_name": "string",

  "paitient_last_name": "string",

  "date_time": "string formatted in yyyy-mm-ddThh:mm:ss",

  "appt_type": "string" one of two options. "R" = Repeat visit, "N" = New Patient
}
```

