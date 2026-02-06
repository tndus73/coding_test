-- 코드를 작성해주세요

select round(sum(case when LENGTH is null then 10 else LENGTH end)/count(*),2) AVERAGE_LENGTH
from FISH_INFO
      