
  create or replace   view MY_DATABASE.RAW_analytics.patients_clean
  
   as (
    SELECT
    patient_id,
    first_name,
    last_name,
    birthdate,
    email,
    phone,
    address,
    gender
FROM MY_DATABASE.RAW.patients
  );

