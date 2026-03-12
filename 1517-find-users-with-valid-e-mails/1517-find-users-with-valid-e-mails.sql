# Write your MySQL query statement below
select user_id, name, mail
from Users
where mail like BINARY '%@leetcode.com' --binary쓰면 정확히 대소문자 구분함.
and mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'