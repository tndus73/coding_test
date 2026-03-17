# Write your MySQL query statement below
/**
select 
    p1.product_id as product1_id,
    p2.product_id as product2_id,
    i.category as product1_category,
    i2.category as product2_category,
    count(*) as customer_count
from ProductPurchases p1
    left join ProductPurchases p2 on p1.user_id = p2.user_id and p1.product_id < p2.product_id
    left join productinfo i on p1.product_id = i.product_id
    left join productinfo i2 on p2.product_id = i2.product_id
group by p1.product_id, p2.product_id
having count(*) >= 3 and product2_id is not null
order by customer_count desc, product1_id, product2_id
**/
with product_purch
as
(
select user_id, PP.product_id, category
from ProductPurchases PP
inner join ProductInfo P on PP.product_id = P.product_id
)
,   total
as
(
select P1.user_id, P1.product_id product1_id, P1.category product1_category
        , P2.product_id product2_id, P2.category product2_category
from product_purch P1
inner join product_purch P2 on P1.user_id=P2.user_id and P1.product_id < P2.product_id
)
select product1_id, product2_id, product1_category, product2_category, count(distinct user_id) customer_count
from total
group by product1_id, product2_id, product1_category, product2_category having count(distinct user_id)>=3
order by customer_count desc, product1_id, product2_id