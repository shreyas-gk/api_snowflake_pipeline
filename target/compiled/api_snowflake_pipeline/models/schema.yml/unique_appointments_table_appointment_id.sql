
    
    

select
    appointment_id as unique_field,
    count(*) as n_records

from MY_DATABASE.RAW_analytics.appointments_table
where appointment_id is not null
group by appointment_id
having count(*) > 1


