with raw_appointments as (
    select * from {{ source('RAW', 'appointments') }}
)

select
    appointment_id,
    patient_id,
    appointment_date::timestamp as appointment_date,
    doctor_name,
    department
from raw_appointments
where appointment_id is not null
