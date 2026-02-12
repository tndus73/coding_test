-- 코드를 입력하세요
with car as
(
SELECT CAR_ID, max(case when to_date('2022-10-16','YYYY-MM-DD') between START_DATE and END_DATE then 1 else 0 end) AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID    
)
select CAR_ID, CASE WHEN AVAILABILITY = 1 THEN '대여중' ELSE '대여 가능' END AS AVAILABILITY
from car
order by CAR_ID desc