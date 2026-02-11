WITH available
AS
(
    SELECT c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR c
    WHERE c.CAR_TYPE IN ('세단', 'SUV')
      AND c.CAR_ID NOT IN (
                          SELECT h.CAR_ID
                          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
                          WHERE h.START_DATE <= TO_DATE('2022-11-30', 'YYYY-MM-DD')
                            AND h.END_DATE   >= TO_DATE('2022-11-01', 'YYYY-MM-DD')
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