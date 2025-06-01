select
    prescription_id,
    patient_id,
    medication_name,
    dosage,
    start_date,
    end_date
from MY_DATABASE.RAW.prescriptions
where start_date is not null