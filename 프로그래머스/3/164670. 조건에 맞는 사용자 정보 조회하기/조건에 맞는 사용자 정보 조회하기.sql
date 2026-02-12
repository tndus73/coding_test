-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, concat(CITY,' ',STREET_ADDRESS1, ' ', STREET_ADDRESS2) 전체주소
        , concat(substr(TLNO,1,3),'-',substr(TLNO,4,4),'-',substr(TLNO,8,4)) 전화번호
from USED_GOODS_BOARD a
inner join USED_GOODS_USER b on b.USER_ID = a.WRITER_ID
group by WRITER_ID having count(BOARD_ID) >=3 
order by USER_ID desc
