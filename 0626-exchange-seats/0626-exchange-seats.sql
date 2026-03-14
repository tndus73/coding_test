# Write your MySQL query statement below
/**
SELECT id,
    CASE
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN student
        WHEN id % 2 = 1 THEN LEAD(student) OVER (ORDER BY id)
        ELSE LAG(student) OVER (ORDER BY id)
    END AS student
FROM Seat
ORDER BY id;
**/

SELECT
    CASE WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
        END AS id
    , student
FROM Seat
ORDER BY id;