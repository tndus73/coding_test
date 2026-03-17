# Write your MySQL query statement below
/**
select 
    user_id,
    round(avg(case when activity_type='free_trial' then activity_duration end),2) as trial_avg_duration,
    round(avg(case when activity_type='paid' then activity_duration end),2) as paid_avg_duration
from 
    UserActivity
group by user_id 
having AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END) IS NOT NULL
order by 
    user_id;
**/

with total
as
(
select user_id, activity_type
        , round(avg(case when activity_type ='free_trial' then activity_duration end),2) trial_avg_duration
        , round(avg(case when activity_type ='paid' then activity_duration end),2) paid_avg_duration
from UserActivity
group by user_id, activity_type
)
select *
from (
    select  user_id , sum(trial_avg_duration) trial_avg_duration,sum(paid_avg_duration) paid_avg_duration
    from total
    group by user_id ) t
where paid_avg_duration is not null
order by user_id