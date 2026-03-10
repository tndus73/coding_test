# Write your MySQL query statement below
/**
select customer_number
from Orders
group by customer_number
order by count(order_number) desc
limit 1;
**/
select customer_number
from (
    select customer_number, count(*) cnt
    from Orders
    group by customer_number
    order by cnt desc
    ) T
limit 1