
  
    

create or replace transient table MY_DATABASE.RAW.appointments_table
    

    
    as (

select
    appointment_id,
    patient_id,
    appointment_date,
    doctor_name,
    department
from MY_DATABASE.RAW.appointments
where appointment_date is not null
    )
;


  