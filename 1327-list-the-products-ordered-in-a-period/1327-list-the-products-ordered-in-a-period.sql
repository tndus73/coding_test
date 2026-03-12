# Write your MySQL query statement below
select product_name, sum(unit) unit
from Products P
inner join Orders O on P.product_id=O.product_id
where date_format(order_date,'%Y-%m')='2020-02'
group by O.product_id having sum(unit)>=100