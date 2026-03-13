# Write your MySQL query statement below
with first
as
(
select player_id, min(event_date) first_date
from Activity
group by player_id
)
select round(count(distinct A.player_id) / (select count(distinct player_id)  from Activity),2) fraction
from Activity A
left join first F on A.player_id = F.player_id
where datediff(event_date,first_date)=1


