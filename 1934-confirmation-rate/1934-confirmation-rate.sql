# Write your MySQL query statement below
/**
select s.user_id, 
round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from signups s
left join confirmations c
on s.user_id=c.user_id
group by s.user_id
**/
with total
as
(
select user_id, round(sum(case when action ='confirmed' then 1 else 0 end)/count(*),2) confirmation_rate 
from Confirmations C
group by user_id
)
select S.user_id, ifnull(confirmation_rate,0) confirmation_rate
from (select distinct user_id from Signups) S
left join total T on S.user_id=T.user_id
