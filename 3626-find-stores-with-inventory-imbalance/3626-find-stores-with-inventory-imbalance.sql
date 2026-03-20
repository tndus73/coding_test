# Write your MySQL query statement below
/**
summary AS (
    SELECT
        store_id,
        MAX(CASE WHEN maxP = 1 THEN product_name END) AS most_exp_product,
        MAX(CASE WHEN maxP = 1 THEN quantity END) AS max_qty,
        MAX(CASE WHEN minP = 1 THEN product_name END) AS cheapest_product,
        MAX(CASE WHEN minP = 1 THEN quantity END) AS min_qty
    FROM total
    GROUP BY store_id
)
**/
with total
as
(
select store_id, product_name, quantity, price
        , row_number() over (partition by store_id order by price desc) maxP
        , row_number() over (partition by store_id order by price) minP
from inventory A
where store_id in (select store_id
                    from inventory
                    group by store_id having count(distinct product_name)>=3)
)

select X.store_id, store_name, location, X.product_name most_exp_product
        , I.product_name cheapest_product
        , round(I.quantity/X.quantity,2) imbalance_ratio
from total X
inner join total I on X.store_id=I.store_id and X.quantity<I.quantity and X.maxp=1 and I.minp=1
inner join stores S on X.store_id=S.store_id 
order by imbalance_ratio desc, store_name
