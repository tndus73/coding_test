# Write your MySQL query statement below
/**
select  book_id, title, author,  genre,  publication_year, current_borrowers
from (
    select I.book_id, title, author,  genre,  publication_year, count(B.book_id) current_borrowers
            , total_copies - count(B.book_id) cur
    from library_books I
    left join borrowing_records B on I.book_id=B.book_id
    where return_date is null
    group by I.book_id) T
where cur =0
order by  current_borrowers desc, title 
**/
select I.book_id, title, author,  genre,  publication_year, count(B.book_id) current_borrowers
from library_books I
left join borrowing_records B on I.book_id=B.book_id
where return_date is null
group by I.book_id having max(total_copies) - count(B.book_id) =0
order by  current_borrowers desc, title 