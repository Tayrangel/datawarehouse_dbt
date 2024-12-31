
    
    

select
    extract_dt as unique_field,
    count(*) as n_records

from "dbdatawarehouse"."public"."fct_commodities"
where extract_dt is not null
group by extract_dt
having count(*) > 1


