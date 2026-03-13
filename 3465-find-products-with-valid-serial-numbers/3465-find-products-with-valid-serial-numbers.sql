# Write your MySQL query statement below
select product_id, product_name, description 
from products
where REGEXP_LIKE(description, '(^| )SN[0-9]{4}-[0-9]{4}( |$)', 'c') /**c는 대소문자 구분**/
order by product_id