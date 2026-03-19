# Write your MySQL query statement below
with total
as
(
select review_id, employee_id, review_date, rating
        , rank() over(partition by employee_id order by review_date desc) last_rn
from performance_reviews
)
, last1
as
(
select employee_id, rating
from total
where last_rn = 1
)
, last2
as
(
select employee_id, rating
from total
where last_rn = 2
)
, last3
as
(
select employee_id, rating
from total
where last_rn = 3
)

select A.employee_id, name, A.rating-C.rating improvement_score
from last1 A
inner join last2 B on A.employee_id=B.employee_id and A.rating>B.rating
inner join last3 C on B.employee_id=C.employee_id and B.rating>C.rating
inner join employees E on A.employee_id=E.employee_id
order by improvement_score desc, name