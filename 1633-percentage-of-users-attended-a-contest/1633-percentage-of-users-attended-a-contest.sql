# Write your MySQL query statement below
select contest_id, round((count(U.user_id)/(select count(*) from Users))*100,2) percentage
from Users U
inner join Register R on U.user_id=R.user_id
group by contest_id
order by percentage desc, contest_id
--round((count(U.user_id)/sum(count(*)) over())*100,2)