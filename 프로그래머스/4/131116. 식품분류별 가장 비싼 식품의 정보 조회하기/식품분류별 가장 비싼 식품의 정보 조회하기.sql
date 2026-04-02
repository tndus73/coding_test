-- 코드를 입력하세요
/**
with category_max
as
(
SELECT CATEGORY, MAX(PRICE) MAX_PRICE
from FOOD_PRODUCT
group by CATEGORY
)
select a.CATEGORY, a.MAX_PRICE, b.PRODUCT_NAME
from category_max a
left join FOOD_PRODUCT b on a.MAX_PRICE = b.PRICE and a.CATEGORY=b.CATEGORY
where a.CATEGORY in  ('과자', '국', '김치', '식용유')
order by MAX_PRICE desc **/

select CATEGORY, PRICE MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT 
where CATEGORY in  ('과자', '국', '김치', '식용유')
and (CATEGORY, PRICE) in (select CATEGORY, max(PRICE) MAX_PRICE
                        from FOOD_PRODUCT
                       group by CATEGORY)
order by MAX_PRICE desc