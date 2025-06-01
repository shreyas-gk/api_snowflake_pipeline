

select
    appointment_id,
    patient_id,
    appointment_date,
    doctor_name,
    department
from MY_DATABASE.RAW.appointments
where appointment_date is not null