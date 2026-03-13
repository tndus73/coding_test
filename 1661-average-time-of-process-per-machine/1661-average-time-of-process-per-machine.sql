# Write your MySQL query statement below
/**
SELECT machine_id,
       ROUND(AVG(process_time),3) AS processing_time
FROM (
    SELECT machine_id,
           process_id,
           MAX(timestamp) - MIN(timestamp) AS process_time
    FROM Activity
    GROUP BY machine_id, process_id
) t
GROUP BY machine_id;
**/
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