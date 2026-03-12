# Write your MySQL query statement below
select  name, sum(T.amount) balance
from Transactions T
left join Users U on U.account = T.account
group by U.name having sum(T.amount) > 10000
