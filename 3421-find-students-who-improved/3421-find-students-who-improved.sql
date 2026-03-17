# Write your MySQL query statement below
with time_fl
as
(
select student_id, subject, exam_date, score
        , rank() over (partition by student_id, subject order by exam_date) first_score
        , rank() over (partition by student_id, subject order by exam_date desc) latest_score
        , count(*) over (partition by student_id, subject) cnt
from Scores S
)
, first
as
(
select student_id, subject, exam_date, score
from time_fl
where first_score =1
)
, last
as
(
select student_id, subject, exam_date, score
from time_fl
where latest_score =1
)

select F.student_id, F.subject, F.score first_score, L.score latest_score
from first F
inner join last L on F.student_id=L.student_id and F.subject=L.subject
where F.exam_date < L.exam_date and F.score < L.score
order by student_id, subject