-- 코드를 입력하세요
with car_rental
as
(
SELECT CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE >= to_date('2022-08-01','YYYY-MM-DD') and START_DATE < to_date('2022-11-01','YYYY-MM-DD')
group by CAR_ID having count(*)>=5
)

select to_char(START_DATE,'MM')*1.0 month, a.CAR_ID, count(*) records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY a
inner join car_rental b on a.CAR_ID=b.CAR_ID
where START_DATE >= to_date('2022-08-01','YYYY-MM-DD') and START_DATE < to_date('2022-11-01','YYYY-MM-DD')
group by to_char(START_DATE,'MM'), a.CAR_ID having count(*)>0
order by month, CAR_ID desc