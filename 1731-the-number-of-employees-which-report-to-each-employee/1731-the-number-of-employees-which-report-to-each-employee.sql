# Write your MySQL query statement below
select E.employee_id, E.name, count(R.employee_id) reports_count, round(avg(R.age)) average_age
from Employees E
inner join Employees R on E.employee_id = R.reports_to
group by E.employee_id, E.name
order by employee_id