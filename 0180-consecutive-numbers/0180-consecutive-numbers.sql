select distinct num ConsecutiveNums
from  
(select num, id-row_number() over(partition by num order by id) gap
from Logs) T
group by num, gap having count(*)>=3
