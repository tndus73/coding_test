-- 코드를 입력하세요
SELECT TRUNC(price, -4), count(*)
from PRODUCT
group by TRUNC(price, -4)
order by TRUNC(price, -4)