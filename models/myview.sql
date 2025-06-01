select
    patient_id,
    first_name,
    last_name,
    email
from {{ ref('my_table') }}
where email like '%@example.com'
