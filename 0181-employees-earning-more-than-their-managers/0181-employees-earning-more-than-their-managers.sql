# Write your MySQL query statement below
/**
직원 급여 > 관리자 급여
T1.managerId = T2.id 조인
id name salary managerID id salary name
**/
select T1.name Employee
from Employee T1
inner join Employee T2 on T1.managerId = T2.id
where T1.salary > T2.salary