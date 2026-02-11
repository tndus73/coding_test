-- 코드를 입력하세요
with total as
(
SELECT SHIPMENT_ID, FLAVOR, TOTAL_ORDER
from FIRST_HALF 
union all  
SELECT SHIPMENT_ID, FLAVOR, TOTAL_ORDER
from JULY 
)
select FLAVOR
from (
    select FLAVOR, sum(TOTAL_ORDER) TOTAL_ORDER
    from total
    group by FLAVOR
    order by TOTAL_ORDER desc
    )
where rownum <= 3