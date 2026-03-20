# Write your MySQL query statement below
with total
as
(
select user_id, reaction, count(*) cnt
from reactions
where user_id in (select user_id from reactions group by user_id having count(distinct content_id)>=5)
group by user_id, reaction
)

select user_id, reaction dominant_reaction, round(cnt/sumcnt,2) reaction_ratio 
from (
select user_id, reaction, cnt
        , row_number() over(partition by user_id order by cnt desc) rn
        , sum(cnt) over(partition by user_id) sumcnt
from total )T
where rn = 1 and cnt/sumcnt>= 0.6
order by reaction_ratio desc, user_id                                                     