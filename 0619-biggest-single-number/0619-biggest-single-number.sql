# Write your MySQL query statement below
/**
with ai
as
(
select num
from MyNumbers
group by num having count(*)=1
)
select max(num) num
from ai
**/
select max(num) num
from (select num
    from MyNumbers
    group by num having count(*)=1) T