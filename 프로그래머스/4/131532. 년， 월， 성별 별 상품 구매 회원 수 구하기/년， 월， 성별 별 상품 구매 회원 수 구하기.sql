-- 코드를 입력하세요
SELECT to_char(SALES_DATE,'YYYY') year, to_char(SALES_DATE,'MM')*1 month, GENDER, count(distinct a.USER_ID) USERS
from ONLINE_SALE a
left join USER_INFO b on a.USER_ID = b.USER_ID
where GENDER is not null
group by to_char(SALES_DATE,'YYYY'), to_char(SALES_DATE,'MM'), GENDER
order by year, month, GENDER