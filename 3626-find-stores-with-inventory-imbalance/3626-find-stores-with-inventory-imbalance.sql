# Write your MySQL query statement below
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
, maxpr
as
(
select store_id, product_name, quantity
from total
where maxP=1
)
, minpr
as
(
select store_id, product_name, quantity
from total
where minP=1
)
select X.store_id, store_name, location, X.product_name most_exp_product
        , I.product_name cheapest_product
        , round(I.quantity/X.quantity,2) imbalance_ratio
from maxpr X
inner join minpr I on X.store_id=I.store_id and X.quantity<I.quantity
inner join stores S on X.store_id=S.store_id 
order by imbalance_ratio desc, store_name
