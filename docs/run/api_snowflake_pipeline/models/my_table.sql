
  
    

create or replace transient table MY_DATABASE.RAW.my_table
    

    
    as (

select
    patient_id,
    first_name,
    last_name,
    birthdate,
    email
from MY_DATABASE.RAW.patients
where birthdate is not null
    )
;


  