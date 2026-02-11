-- 코드를 입력하세요

select a.PRODUCT_CODE, T_SALES_AMOUNT*PRICE SALES
from PRODUCT a
inner join (
            SELECT PRODUCT_ID, sum(SALES_AMOUNT) T_SALES_AMOUNT
            from OFFLINE_SALE
            group by PRODUCT_ID
            ) b on a.PRODUCT_ID = b.PRODUCT_ID
order by SALES desc, a.PRODUCT_CODE