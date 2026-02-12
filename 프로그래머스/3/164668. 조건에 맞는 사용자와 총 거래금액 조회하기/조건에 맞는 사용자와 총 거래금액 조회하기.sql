-- 코드를 입력하세요
with done
as
(
SELECT a.WRITER_ID, sum(price) TOTAL_SALES
from USED_GOODS_BOARD a
where STATUS ='DONE'
group by a.WRITER_ID having sum(price) >= 700000
)

select USER_ID, NICKNAME, TOTAL_SALES
from done a
left join USED_GOODS_USER b on a.WRITER_ID = b.USER_ID
order by TOTAL_SALES