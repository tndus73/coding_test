with first
as
(
select player_id , min(event_date) first_date
from Activity
group by player_id
)
select round(count(distinct F.player_id)/ count(distinct A.player_id),2) fraction 
from Activity A
left join  first F on A.player_id = F.player_id and A.event_date = F.first_date + interval 1 day
