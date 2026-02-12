-- 코드를 입력하세요
with book_S 
as
(
SELECT b.AUTHOR_ID, CATEGORY, sum(PRICE * SALES) TOTAL_SALES
from BOOK_SALES a
left join BOOK b on a.BOOK_ID = b.BOOK_ID
where SALES_DATE >= to_date('2022-01-01','YYYY-MM-DD') and SALES_DATE < to_date('2022-02-01','YYYY-MM-DD')
group by b.AUTHOR_ID, CATEGORY
)
select a.AUTHOR_ID, AUTHOR_NAME, CATEGORY, TOTAL_SALES
from book_S a
inner join AUTHOR b on a.AUTHOR_ID = b.AUTHOR_ID
order by a.AUTHOR_ID, CATEGORY desc
