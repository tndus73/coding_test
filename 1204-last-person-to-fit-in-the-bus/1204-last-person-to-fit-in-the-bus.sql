# Write your MySQL query statement below


select person_name
from (
select person_id, person_name, turn, sum(weight) over(order by turn) T_sum
from Queue ) T
where T_sum <=1000
order by turn desc
limit 1
