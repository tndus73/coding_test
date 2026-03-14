# Write your MySQL query statement below
/**
select product_id, year as first_year, quantity, price 
from sales where (product_id, year) in (
    select product_id, min(year)
    from sales
    group by product_id
)
**/
select S.product_id, first_year, quantity, price
from Sales S left join  ( select product_id, min(year) first_year
                            from Sales
                            group by product_id ) T on S.product_id=T.product_id
where first_year = year