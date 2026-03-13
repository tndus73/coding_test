# Write your MySQL query statement below
select Department, Employee, salary
from(
select D.name Department, E.name Employee, salary, dense_rank() over (partition by D.id order by salary desc) rnk
from Employee E
inner join Department D on E.departmentId = D.id ) T
where rnk =1