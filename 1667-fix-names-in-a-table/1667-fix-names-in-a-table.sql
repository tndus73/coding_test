# Write your MySQL query statement below
/** CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(name,2))) **/
select user_id, concat(upper(left(name,1)),lower(substring(name,2))) name
from Users
order by user_id