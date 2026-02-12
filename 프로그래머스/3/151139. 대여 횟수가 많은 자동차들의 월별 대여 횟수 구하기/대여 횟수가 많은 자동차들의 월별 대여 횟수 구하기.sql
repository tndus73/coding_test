-- 코드를 입력하세요
-- 코드를 입력하세요
with car_rental
as
(
SELECT CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE >= '2022-08-01' and START_DATE < '2022-11-01'
group by CAR_ID having count(*)>=5
)

select date_format(START_DATE,'%m')*1.0 month, a.CAR_ID, count(*) records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY a
inner join car_rental b on a.CAR_ID=b.CAR_ID
where START_DATE >= '2022-08-01' and START_DATE < '2022-11-01'
group by date_format(START_DATE,'%m'), a.CAR_ID having count(*)>0
order by month, CAR_ID desc