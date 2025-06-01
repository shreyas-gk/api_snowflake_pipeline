with raw_prescriptions as (
    select * from {{ source('RAW', 'prescriptions') }}
)

select
    prescription_id,
    patient_id,
    medication_name,
    dosage,
    start_date::date as start_date,
    end_date::date as end_date
from raw_prescriptions
where prescription_id is not null
