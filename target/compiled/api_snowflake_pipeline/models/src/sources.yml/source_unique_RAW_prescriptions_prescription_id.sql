
    
    

select
    prescription_id as unique_field,
    count(*) as n_records

from MY_DATABASE.RAW.prescriptions
where prescription_id is not null
group by prescription_id
having count(*) > 1


