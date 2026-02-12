-- 코드를 입력하세요
with hour_T
as
(
select level-1 hour
from dual
connect by level <= 24
)

SELECT a.hour, count(b.DATETIME) 	COUNT
from hour_T a 
left join ANIMAL_OUTS b ON TO_CHAR(b.datetime, 'HH24') = LPAD(a.hour, 2, '0')
group by a.hour
order by hour