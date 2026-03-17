# Write your MySQL query statement below
/**
with temp as (
select student_id,subject,
        first_value(score) over (partition by student_id,subject order by exam_date) as f1 ,
        first_value(score) over(partition by student_id,subject order by exam_date desc) as f2
from scores
)

select  student_id, subject,f1 as first_score, f2 as latest_score 
from temp where f1<f2
group by 1,2
order by 1,2
**/
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