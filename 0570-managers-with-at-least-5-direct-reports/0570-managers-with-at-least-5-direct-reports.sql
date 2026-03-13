# Write your MySQL query statement below
/**
SELECT E2.name
FROM Employee E1
JOIN Employee E2
ON E1.managerId = E2.id
GROUP BY E1.managerId
HAVING COUNT(*) >= 5;
**/
select name
from  Employee
where id in (
            select managerId
            from Employee
            group by managerId having count(*)>=5 )