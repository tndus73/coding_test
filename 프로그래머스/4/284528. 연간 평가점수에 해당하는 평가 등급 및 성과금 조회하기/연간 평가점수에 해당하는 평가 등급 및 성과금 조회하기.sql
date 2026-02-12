-- 코드를 작성해주세요
with Bonus_E
as
(
select EMP_NO
        , case when avg(SCORE) >= 96 then 'S'
               when avg(SCORE) >= 90 then 'A'
               when avg(SCORE) >= 80 then 'B'
               else 'C'
               end GRADE
        , case when avg(SCORE) >= 96 then 0.2
               when avg(SCORE) >= 90 then 0.15
               when avg(SCORE) >= 80 then 0.1
               else 0
               end B
from HR_GRADE
group by EMP_NO
)

select a.EMP_NO, EMP_NAME, GRADE, 	SAL*B	BONUS
from HR_EMPLOYEES a
left join Bonus_E b on a.EMP_NO= b.EMP_NO
order by EMP_NO