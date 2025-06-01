{{ config(materialized='table') }}

select
    appointment_id,
    patient_id,
    appointment_date,
    doctor_name,
    department
from {{ source('RAW', 'appointments') }}
where appointment_date is not null
