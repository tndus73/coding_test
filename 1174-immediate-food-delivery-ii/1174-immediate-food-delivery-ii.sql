# Write your MySQL query statement below
select round((sum(case when first_order=customer_pref_delivery_date then 1 else 0 end) / count(distinct D.customer_id))*100,2)  immediate_percentage 
from Delivery D left join (
    select customer_id, min(order_date) first_order
    from Delivery
    group by customer_id) T on D.customer_id = T.customer_id