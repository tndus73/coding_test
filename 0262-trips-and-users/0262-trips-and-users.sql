# Write your MySQL query statement below
select request_at Day
        , round(sum(case when status like 'cancelled%' then 1 else 0 end)/count(*),2) 'Cancellation Rate'
from (
select id, status, request_at 
from Trips
where client_id in (select users_id from Users where banned='No')
and driver_id in (select users_id from Users where banned='No')
and request_at between '2013-10-01' and '2013-10-03'
)T
group by request_at
