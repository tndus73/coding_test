# Write your MySQL query statement below
with uni_vis
as
(
select visited_on, sum(amount) sum_amount
from Customer
group by visited_on
)

select visited_on, SUM(sum_amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) amount
        ,round(AVG(sum_amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) average_amount
from uni_vis
order by visited_on
LIMIT 100000 OFFSET 6