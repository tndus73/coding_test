# Write your MySQL query statement below
/**
SELECT ROUND(SUM(tiv_2016),2) tiv_2016
FROM (
    SELECT *,
           COUNT(*) OVER(PARTITION BY tiv_2015) c1,
           COUNT(*) OVER(PARTITION BY lat,lon) c2
    FROM Insurance
) T
WHERE c1>1 AND c2=1;
**/
select round(sum(tiv_2016),2) tiv_2016
from Insurance I
where (lat,lon) not in (select lat,lon 
                        from Insurance
                        group by lat,lon having count(*)>1)
and tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(*)>1)