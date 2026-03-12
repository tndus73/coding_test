# Write your MySQL query statement below
select unique_id, name 
from Employees E
left join EmployeeUNI EI on E.id = EI.id   