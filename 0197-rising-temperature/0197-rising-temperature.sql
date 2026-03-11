# Write your MySQL query statement below
/**
이건 쿼리는 중간에 날짜 없으면 전날이 아닌데 판단할 수 있는 오류 존
with we_T
as
(
select id, recordDate, temperature, lag(temperature) over(order by recordDate) as Pre_tem
from Weather
)
select id Id
from we_T
where  temperature > Pre_tem
**/
SELECT T1.id
FROM Weather T1
inner join Weather T2 ON DATEDIFF(T1.recordDate, T2.recordDate) = 1
                            AND T1.temperature > T2.temperature;