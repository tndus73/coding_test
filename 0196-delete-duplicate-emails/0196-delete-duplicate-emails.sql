/**
select id, email
from (
select id, email
        , row_number() over(partition by email order by id) rn
from Person) T
where rn=1 **/
DELETE p1 FROM Person p1
JOIN Person p2 
ON p1.email = p2.email AND p1.id > p2.id;