/**
WITH available
AS
(
    SELECT c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR c
    WHERE c.CAR_TYPE IN ('세단', 'SUV')
      AND c.CAR_ID NOT IN (
                          SELECT h.CAR_ID
                          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
                          WHERE h.START_DATE <= '2022-11-30'
                            AND h.END_DATE   >= '2022-11-01'
                            )
)
,   priced
AS
(
    SELECT
        a.CAR_ID,
        a.CAR_TYPE,
        ROUND(a.DAILY_FEE * 30 * (1 - p.DISCOUNT_RATE / 100)) AS FEE
    FROM available a
    inner JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
      ON p.CAR_TYPE = a.CAR_TYPE
     AND p.DURATION_TYPE = '30일 이상'
)
SELECT CAR_ID, CAR_TYPE, FEE
FROM priced
WHERE FEE >= 500000
  AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;
**/
# 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차
select  CAR_ID, CAR_TYPE, round(FEE) FEE
from(
select C.CAR_ID, C.CAR_TYPE, DAILY_FEE*30*(1-DISCOUNT_RATE/100) FEE
from CAR_RENTAL_COMPANY_CAR C
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P on C.CAR_TYPE=P.CAR_TYPE and DURATION_TYPE='30일 이상'
where C.CAR_TYPE in ('세단','SUV')
and C.CAR_ID not in (select CAR_ID 
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 where START_DATE<'2022-11-30' and END_DATE>'2022-11-01'))T
where FEE >= 500000 and FEE < 2000000
order by FEE desc, CAR_TYPE, CAR_ID desc