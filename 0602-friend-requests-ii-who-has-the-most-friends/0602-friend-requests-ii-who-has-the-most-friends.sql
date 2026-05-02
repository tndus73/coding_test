select id, count(*) num
from (select requester_id id
        from RequestAccepted

        union all 

        select accepter_id id
        from RequestAccepted)T
group by id
order by num desc
limit 1
