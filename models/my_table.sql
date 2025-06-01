{{ config(materialized='table') }}

select
    patient_id,
    first_name,
    last_name,
    birthdate,
    email
from {{ source('RAW', 'patients') }}
where birthdate is not null
