# Write your MySQL query statement below
with total
as
(
select *, action_date - row_number() over(partition by user_id, action order by action_date) gap
from activity
)
select user_id, action, count(*) streak_length, min(action_date) start_date, max(action_date) end_date
from total
group by user_id, gap having count(*)>=5
order by streak_length desc, user_id