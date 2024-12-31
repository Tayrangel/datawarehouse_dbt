
    
    

select
    Date as unique_field,
    count(*) as n_records

from "dbdatawarehouse"."public"."commodities"
where Date is not null
group by Date
having count(*) > 1

