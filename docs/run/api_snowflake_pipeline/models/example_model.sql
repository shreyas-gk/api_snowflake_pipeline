
  create or replace   view MY_DATABASE.RAW.example_model
  
   as (
    select * from raw.patients limit 10
  );

