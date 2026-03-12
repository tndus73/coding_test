# Write your MySQL query statement below
select user_id, name, mail
from Users
where mail like BINARY '%@leetcode.com' and mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'