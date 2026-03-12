# Write your MySQL query statement below
select name, ifnull(sum(distance),0) travelled_distance
from Users U
left join Rides R on R.user_id= U.id
group by user_id, name
order by travelled_distance desc, name