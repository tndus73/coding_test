# Write your MySQL query statement below
with total
as
(
select id, visit_date, people
        , id-row_number() over(order by id) grp
from Stadium
where people>=100
)
select id, visit_date, people 
from total
where grp in(select grp
            from total
            group by grp having count(*)>=3)
 order by visit_date