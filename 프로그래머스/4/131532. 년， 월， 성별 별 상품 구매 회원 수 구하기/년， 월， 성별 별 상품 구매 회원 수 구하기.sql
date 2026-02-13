-- 코드를 입력하세요
SELECT year(SALES_DATE) year, month(SALES_DATE) month, GENDER, count(distinct a.USER_ID) USERS
from ONLINE_SALE a
left join USER_INFO b on a.USER_ID = b.USER_ID
where GENDER is not null
group by year(SALES_DATE), month(SALES_DATE), GENDER
order by year, month, GENDER