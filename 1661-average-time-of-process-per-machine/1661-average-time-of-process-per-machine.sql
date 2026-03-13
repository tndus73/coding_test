# Write your MySQL query statement below
with ai
as
(
select machine_id, process_id, max(timestamp)-min(timestamp) pro_time1
from Activity
group by machine_id, process_id
)
select machine_id, round(sum(pro_time1)/count(*),3) processing_time
from ai
group by machine_id