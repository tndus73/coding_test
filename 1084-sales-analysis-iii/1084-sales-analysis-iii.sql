# Write your MySQL query statement below
/**
select distinct P.product_id, product_name
from Product P
inner join Sales S on P.product_id=S.product_id
where sale_date between '2019-01-01' and '2019-03-31'
and P.product_id not in (select product_id
                     from Sales
                     where sale_date < '2019-01-01' or sale_date > '2019-03-31')
**/
SELECT P.product_id, P.product_name
FROM Product P
JOIN Sales S
  ON P.product_id = S.product_id
GROUP BY P.product_id, P.product_name
HAVING MIN(S.sale_date) >= '2019-01-01'
   AND MAX(S.sale_date) <= '2019-03-31';