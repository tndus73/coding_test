
select Department, Employee, salary
from (
select D.name Department, E.name Employee
        , salary, rank() over(partition by D.name order by salary desc) rn
from Employee E
inner join Department D on E.departmentId=D.id ) T
where rn = 1