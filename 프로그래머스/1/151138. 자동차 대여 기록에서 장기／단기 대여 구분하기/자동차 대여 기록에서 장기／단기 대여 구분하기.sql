-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE, '%Y-%m-%d')
        , DATE_FORMAT(END_DATE, '%Y-%m-%d')
        , case when datediff(END_DATE,START_DATE)>=29 then '장기 대여'
                else '단기 대여'
                end RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(START_DATE,'%Y-%m')='2022-09'
order by HISTORY_ID desc