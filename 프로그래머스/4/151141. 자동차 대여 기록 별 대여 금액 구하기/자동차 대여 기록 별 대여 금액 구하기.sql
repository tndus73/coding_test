-- 코드를 입력하세요

with car_his
as
(
SELECT a.HISTORY_ID, b.CAR_ID, b.CAR_TYPE, b.DAILY_FEE, datediff(END_DATE,START_DATE)+1 duration
from   CAR_RENTAL_COMPANY_RENTAL_HISTORY a
left join CAR_RENTAL_COMPANY_CAR b on a.CAR_ID=b.CAR_ID
where b.CAR_TYPE = '트럭'
)    
select HISTORY_ID, FLOOR((DAILY_FEE * (1 - ifnull(DISCOUNT_RATE,0)/100)) * duration) FEE
from car_his a
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN b on a.CAR_TYPE = b.CAR_TYPE 
    and DURATION_TYPE = case when a.duration >= 90 then '90일 이상'
                            when a.duration >= 30 then '30일 이상'
                            when a.duration >= 7 then '7일 이상'
                            else null
                            end
order by FEE desc, HISTORY_ID desc