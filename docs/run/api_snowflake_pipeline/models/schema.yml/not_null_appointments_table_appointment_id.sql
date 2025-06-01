
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select appointment_id
from MY_DATABASE.RAW_analytics.appointments_table
where appointment_id is null



  
  
      
    ) dbt_internal_test