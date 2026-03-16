WITH user_cnt AS (
    SELECT u.name, COUNT(*) AS cnt
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY u.user_id, u.name
)
, movie_avg 
AS (
    SELECT m.title, AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE DATE_FORMAT(mr.created_at, '%Y-%m') = '2020-02'
    GROUP BY m.movie_id, m.title
)
SELECT results
FROM (
    SELECT name AS results
    FROM user_cnt
    ORDER BY cnt DESC, name
    LIMIT 1)T

UNION ALL

SELECT results
FROM (
    SELECT title AS results
    FROM movie_avg
    ORDER BY avg_rating DESC, title
    LIMIT 1)S