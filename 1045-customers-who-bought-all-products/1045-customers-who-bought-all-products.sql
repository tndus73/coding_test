# Write your MySQL query statement below
with id_pr
as
(
select customer_id, count(distinct product_key) prodct_key
from Customer C
group by customer_id
)
select customer_id
from id_pr
where prodct_key in (select count(*) from Product P)