-- 코드를 입력하세요
/**
with total as
(
SELECT SHIPMENT_ID, FLAVOR, TOTAL_ORDER
from FIRST_HALF 
union all  
SELECT SHIPMENT_ID, FLAVOR, TOTAL_ORDER
from JULY 
)


    select FLAVOR
    from total
    group by FLAVOR
    order by sum(TOTAL_ORDER) desc
    limit 3
**/
select FLAVOR
from(
    select FLAVOR, TOTAL_ORDER
    from FIRST_HALF
    union 
    select FLAVOR, TOTAL_ORDER
    from JULY) T
group by FLAVOR   
order by sum(TOTAL_ORDER) desc
limit 3
    
    