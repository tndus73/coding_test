# Write your MySQL query statement below
select name, bonus
from Employee T1
left join Bonus T2 on T1.empId = T2.empId
where T2.bonus is null or T2.bonus < 1000