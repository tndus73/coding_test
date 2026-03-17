# Write your MySQL query statement below
with total
as
(
select case when month(sale_date) in (12, 1, 2) then 'Winter'
            when month(sale_date) in (3, 4, 5) then 'Spring'
            when month(sale_date) in (6, 7, 8) then 'Summer'
            when month(sale_date) in (9, 10, 11) then 'Fall'
            end season
       , category,  sum(quantity) total_quantity, sum(quantity*price) total_revenue                    
from sales S
left join products P on S.product_id=P.product_id
group by season, category
)

select season, category, total_quantity, total_revenue
from(
select season, category, total_quantity, total_revenue
        , rank() over (partition by season order by total_quantity desc, total_revenue desc) rn
from total) T
where rn = 1
order by 1