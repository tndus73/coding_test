-- 코드를 입력하세요

with R_CNT
as
(
select MEMBER_ID
from (
    SELECT MEMBER_ID
            , rank() over (order by count(MEMBER_ID) desc) rn
    from REST_REVIEW
    group by MEMBER_ID
    ) t
where rn=1    
) 

select MEMBER_NAME, REVIEW_TEXT, date_format(a.REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE
from REST_REVIEW a
inner join R_CNT b on a.MEMBER_ID = b.MEMBER_ID
inner join MEMBER_PROFILE c on a.MEMBER_ID = c.MEMBER_ID
order by REVIEW_DATE, REVIEW_TEXT