with raw_patients as (
    select * from MY_DATABASE.RAW.patients
)

select
    patient_id,
    first_name,
    last_name,
    birthdate::date as birthdate,
    email,
    phone,
    address,
    gender
from raw_patients
where patient_id is not null