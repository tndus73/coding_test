# Write your MySQL query statement below
/**
SELECT e.employee_id
FROM Employees e
WHERE e.salary < 30000
AND NOT EXISTS (
    SELECT 1
    FROM Employees m
    WHERE m.employee_id = e.manager_id
)
ORDER BY e.employee_id;
**/
select employee_id
from Employees
where salary < 30000
and manager_id NOT IN (SELECT employee_id FROM Employees)
order by employee_id