/**-- 코드를 입력하세요
with user_2021
as
(
select USER_ID
from USER_INFO
where JOINED >= TO_DATE('2021-01-01','YYYY-MM-DD')
and JOINED < TO_DATE('2022-01-01','YYYY-MM-DD')
)
,   T_user
AS
(
  SELECT COUNT(*) total_cnt
  FROM user_2021
)
,   T_product
as
(
select to_char(SALES_DATE,'YYYY') Year, to_char(SALES_DATE,'MM')*1 Month, count(distinct a.USER_ID) Pur_user
from ONLINE_SALE a
left join user_2021 b on a.USER_ID = b.USER_ID
where b.USER_ID is not null   
group by to_char(SALES_DATE,'YYYY'), to_char(SALES_DATE,'MM')*1
)

select year, month, pur_user PURCHASED_USERS, round(pur_user/total_cnt,1) PUCHASED_RATIO
from T_product, T_user
order by Year, Month
**/

SELECT TO_CHAR(O.SALES_DATE, 'YYYY') AS YEAR,
       TO_NUMBER(TO_CHAR(O.SALES_DATE, 'MM')) AS MONTH,
       COUNT(DISTINCT O.USER_ID) AS PURCHASED_USERS,
       ROUND(COUNT(DISTINCT O.USER_ID)*1 / (
               SELECT COUNT(*)
               FROM USER_INFO
               WHERE JOINED >= DATE '2021-01-01'
                 AND JOINED < DATE '2022-01-01'
           ),1) AS PURCHASED_RATIO
FROM USER_INFO U
JOIN ONLINE_SALE O ON U.USER_ID = O.USER_ID
WHERE U.JOINED >= DATE '2021-01-01'
  AND U.JOINED < DATE '2022-01-01'
GROUP BY TO_CHAR(O.SALES_DATE, 'YYYY'),
         TO_CHAR(O.SALES_DATE, 'MM')
ORDER BY YEAR, MONTH;