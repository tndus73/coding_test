# Write your MySQL query statement below
select  name, sum(T.amount) balance
from Users U
left join Transactions T on U.account = T.account
group by U.name having sum(T.amount) > 10000
