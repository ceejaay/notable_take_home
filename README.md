## Notable Take-home project April 2, 2022
### By [Chad Jemmett]()

#### Instructions

Clone the repository on your local machine.

Create the environment.

run `pip -r requirements.txt`

`./manage.py makemigrations`
`./manage.py migrate`
`./manage.py runserver`

Navigate to [localhost:8000/doctors/](localhost:8000/doctors/)


#### Endpoints
`/doctors/` 
* `GET` a list of all doctors.
* `POST` Create a new doctor.


`/doctors/<pk number>/` Get an indivisual doctor.

`/doctors/<pk number>/appointments/`  Make a `GET`request and get a list of appointments by doctor.
`POST` request to create and apointment for the doctor.

Data format
```
{"patient_first_name": "string",

"paitient_last_name": "string",

"date_time": "string formatted in yyyy-mm-ddThh:mm:ss",

"appt_type": "string" one of two options. "R" = Repeat visit, "N" = New Patient
}
```

