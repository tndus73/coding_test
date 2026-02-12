-- 코드를 입력하세요
SELECT CATEGORY, sum(SALES) 	TOTAL_SALES
from BOOK_SALES a
left join BOOK b on a.BOOK_ID= b.BOOK_ID
where to_char(SALES_DATE,'YYYY-MM') = '2022-01'
group by CATEGORY
order by CATEGORY
