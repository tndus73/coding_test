-- 코드를 입력하세요
SELECT to_char(DATETIME,'HH24')*1.0 hour, count(*) COUNT
from ANIMAL_OUTS
where to_char(DATETIME,'HH24') >= '09' and to_char(DATETIME,'HH24')<'20'
group by to_char(DATETIME,'HH24')
order by hour