-- 코드를 작성해주세요
with max_EMP
as
(
select EMP_NO, sum(SCORE) SCORE
from HR_GRADE
group by EMP_NO
order by SCORE desc
limit 1 
)

select SCORE, a.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES a
inner join max_EMP b on a.EMP_NO=b.EMP_NO