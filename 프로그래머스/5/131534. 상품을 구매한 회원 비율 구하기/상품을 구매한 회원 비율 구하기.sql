-- 코드를 입력하세요
with T_2021 as
(
SELECT USER_ID
from USER_INFO
where JOINED >= '2021-01-01' and JOINED < '2022-01-01'
)
,   T_cnt as
(
SELECT count(distinct USER_ID) total_user
from T_2021
)

select year(SALES_DATE) year, month(SALES_DATE)*1 month , count(distinct a.USER_ID) PURCHASED_USERS
        , round(count(distinct a.USER_ID)*1/total_user,1) PUCHASED_RATIO
from ONLINE_SALE a , T_cnt b
    
where USER_ID in (select USER_ID
                from T_2021)
group by  year(SALES_DATE), month(SALES_DATE)*1    
order by year, month