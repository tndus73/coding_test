# Write your MySQL query statement below
select distinct num ConsecutiveNums 
from (
select num,  id - DENSE_RANK() OVER(PARTITION BY num ORDER BY id) AS grp
from Logs ) T
group by num, grp  having count(*)>=3
