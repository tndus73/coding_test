# Write your MySQL query statement below
select Department, Employee, Salary
from (
select D.name Department, E.name Employee, Salary
        , dense_rank() over(partition by E.departmentId order by salary desc) rn
from Employee E
inner join Department D on E.departmentId=D.id) T
where rn <=3