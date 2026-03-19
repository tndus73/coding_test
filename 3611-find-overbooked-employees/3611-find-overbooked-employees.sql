# Write your MySQL query statement below
with total
as
(
select employee_id, YEARWEEK(meeting_date,1) perweek, sum(duration_hours) totalhours
from meetings
group by employee_id, YEARWEEK(meeting_date,1) -- 1은 월요일, 0은 일요일
)

select T.employee_id, employee_name, department, count(*) meeting_heavy_weeks
from total T
inner join employees E on T.employee_id=E.employee_id
where totalhours>20
group by T.employee_id, employee_name, department having count(*) >1
order by meeting_heavy_weeks desc, employee_name 