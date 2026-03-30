-- 코드를 입력하세요
/**
with R_CNT
as
(
select MEMBER_ID
from (
    SELECT MEMBER_ID
            , rank() over (order by count(MEMBER_ID) desc) rn
    from REST_REVIEW
    group by MEMBER_ID
    ) t -- mysql은 서브쿼리에 as명칭 해줘야함
where rn=1    
) 

select MEMBER_NAME, REVIEW_TEXT, date_format(a.REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE
from REST_REVIEW a
inner join R_CNT b on a.MEMBER_ID = b.MEMBER_ID
inner join MEMBER_PROFILE c on a.MEMBER_ID = c.MEMBER_ID
order by REVIEW_DATE, REVIEW_TEXT
**/
with manyr
as
(
select MEMBER_ID, dense_rank() over(order by count(*) desc) rn
from REST_REVIEW
group by MEMBER_ID
)

select MEMBER_NAME,	REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d')
from MEMBER_PROFILE M 
inner join manyr T on M.MEMBER_ID=T.MEMBER_ID
inner join REST_REVIEW R on M.MEMBER_ID=R.MEMBER_ID
where rn = 1
order by REVIEW_DATE, REVIEW_TEXT