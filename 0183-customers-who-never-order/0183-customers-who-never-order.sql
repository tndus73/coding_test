# Write your MySQL query statement below
/**
customers T1 left join Orders T2 on T1.id = T2.CustomerId
T2 id가 없는 고객
**/
select T1.name Customers 
from customers T1
left join Orders T2 on T1.id = T2.CustomerId
where T2.id is null