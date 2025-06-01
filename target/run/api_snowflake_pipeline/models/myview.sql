
  create or replace   view MY_DATABASE.RAW.myview
  
   as (
    select
    patient_id,
    first_name,
    last_name,
    email
from MY_DATABASE.RAW.my_table
where email like '%@example.com'
  );

