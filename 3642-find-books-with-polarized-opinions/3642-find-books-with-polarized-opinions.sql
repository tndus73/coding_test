# Write your MySQL query statement below
with total
as
(
select book_id, min(session_rating) minrat, max(session_rating) maxrat
        , count(case when session_rating >= 4 or session_rating <=2 then 1 end) countrat
        , count(*) totalcountrat
from reading_sessions
group by book_id having count(*)>=5 and max(session_rating)>=4 and min(session_rating)<=2 )

select M.book_id, title, author, genre, pages, maxrat-minrat rating_spread, round(countrat/totalcountrat,2) polarization_score
from total M
inner join books B on M.book_id=B.book_id
where round(countrat/totalcountrat,2) >= 0.6
order by polarization_score desc, title desc
