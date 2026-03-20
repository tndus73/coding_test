# Write your MySQL query statement below
select customer_id, count(*) total_orders
        , round((sum(case WHEN DATE_FORMAT(order_timestamp, '%H:%i') BETWEEN '11:00' AND '14:00'
            OR DATE_FORMAT(order_timestamp, '%H:%i') BETWEEN '18:00' AND '21:00' then 1 end) / count(*))*100) peak_hour_percentage
        , round(avg(order_rating),2) average_rating
from restaurant_orders
group by customer_id having count(*)>=3 and avg(order_rating)>=4 
and count(order_rating)/count(*)>=0.5
and sum(case WHEN DATE_FORMAT(order_timestamp, '%H:%i') BETWEEN '11:00' AND '14:00'
            OR DATE_FORMAT(order_timestamp, '%H:%i') BETWEEN '18:00' AND '21:00' then 1 end) / count(*) >= 0.6 
order by average_rating desc, customer_id desc

