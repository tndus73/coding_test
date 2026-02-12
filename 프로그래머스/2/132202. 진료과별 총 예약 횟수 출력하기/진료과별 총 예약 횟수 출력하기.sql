-- 코드를 입력하세요
SELECT MCDP_CD "진료과 코드", count(*) "5월예약건수"
from APPOINTMENT
where APNT_YMD >=TO_DATE('2022-05-01','YYYY-MM-DD') and APNT_YMD < TO_DATE('2022-06-01','YYYY-MM-DD')
group by MCDP_CD
order by "5월예약건수", "진료과 코드"