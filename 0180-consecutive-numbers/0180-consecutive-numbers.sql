# Write your MySQL query statement below
/**
select distinct num ConsecutiveNums 
from (
select num,  id - DENSE_RANK() OVER(PARTITION BY num ORDER BY id) AS grp
from Logs ) T
group by num, grp  having count(*)>=3
**/
select distinct num ConsecutiveNums 
from(
select num, lag(num,1) over(order by id) lag1
        , lag(num,2) over(order by id) lag2
from Logs)T
where num=lag1 and num=lag2
