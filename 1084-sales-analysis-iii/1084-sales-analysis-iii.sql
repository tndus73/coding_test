# Write your MySQL query statement below
select distinct P.product_id, product_name
from Product P
inner join Sales S on P.product_id=S.product_id
where sale_date between '2019-01-01' and '2019-03-31'
and P.product_id not in (select product_id
                     from Sales
                     where sale_date < '2019-01-01' or sale_date > '2019-03-31')