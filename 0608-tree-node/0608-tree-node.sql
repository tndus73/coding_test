# Write your MySQL query statement below
select ID, case when p_id is null then 'Root'
                when not exists (select 'x' from Tree T2 where T1.id=T2.p_id)   then 'Leaf'
                else 'Inner'
                end type
from Tree T1