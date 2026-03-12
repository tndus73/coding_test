# Write your MySQL query statement below
select S.student_id, S.student_name, SU.subject_name , count(E.subject_name) attended_exams
from Students S
cross join Subjects su
left join Examinations E on E.student_id=S.student_id AND SU.subject_name = E.subject_name
group by S.student_id, S.student_name, SU.subject_name
order by S.student_id, S.student_name, SU.subject_name