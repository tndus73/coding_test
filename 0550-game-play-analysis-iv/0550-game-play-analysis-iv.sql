with first
as
(
select player_id , min(event_date) first_date
from Activity
group by player_id
)
select round(count(A.player_id)/ count(F.player_id),2) fraction 
from first F
left join Activity A on A.player_id = F.player_id and A.event_date = F.first_date + interval 1 day
/**
select round(count(case when datediff(event_date, first_date) = 1 then 1 end) / count(distinct player_id), 2) as fraction
from (
  select player_id,
         event_date,
         min(event_date) over (partition by player_id) as first_date
  from Activity
) t;
**/