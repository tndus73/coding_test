# Write your MySQL query statement below
with ai
as
(select product_id, new_price, change_date, rank() over (partition by product_id order by change_date desc) rn
from Products
where change_date <= '2019-08-16'
)  
, ak
as
(
select distinct product_id 
from Products
)
select K.product_id, ifnull(new_price,10) price
from ak K
left join ai i on K.product_id = i.product_id and rn=1