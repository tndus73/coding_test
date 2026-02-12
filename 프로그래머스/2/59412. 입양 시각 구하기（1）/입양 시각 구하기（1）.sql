-- 코드를 입력하세요
SELECT date_Format(DATETIME,'%H') hour, count(*) COUNT
from ANIMAL_OUTS
where date_Format(DATETIME,'%H') >= '09' and date_Format(DATETIME,'%H')<'20'
group by date_Format(DATETIME,'%H')
order by hour