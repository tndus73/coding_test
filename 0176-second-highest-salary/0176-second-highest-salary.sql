# Write your MySQL query statement below
select (
    select distinct salary SecondHighestSalary
    from (
    select  salary, dense_rank() over(order by salary desc) SecondHighestSalary
    from Employee
    order by salary desc  ) T
    where SecondHighestSalary=2 ) SecondHighestSalary
