
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select prescription_id
from MY_DATABASE.RAW.prescriptions
where prescription_id is null



  
  
      
    ) dbt_internal_test