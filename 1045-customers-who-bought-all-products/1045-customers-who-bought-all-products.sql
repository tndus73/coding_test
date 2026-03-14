# Write your MySQL query statement below

select customer_id
from (
    select customer_id, count(distinct product_key) prodct_key
    from Customer C
    group by customer_id
    )
where prodct_key in (select count(*) from Product P)