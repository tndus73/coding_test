# Write your MySQL query statement below
/**
SELECT 'Low Salary' AS category,
       COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000

UNION ALL

SELECT 'Average Salary',
       COUNT(*)
FROM Accounts
WHERE income BETWEEN 20000 AND 50000

UNION ALL

SELECT 'High Salary',
       COUNT(*)
FROM Accounts
WHERE income > 50000;
**/
with cnt
as
(
select account_id, case when income>50000 then "High Salary"
                        when income>=20000 then "Average Salary"
                        else "Low Salary"
                        end category
from Accounts)
, total
as
(
select category, count(*) accounts_count
from cnt
group by category
)
select S.category, ifnull(accounts_count,0) accounts_count
from (select "High Salary" category 
      union all 
      select "Average Salary" category 
      union all 
      select "Low Salary" category) S
left join total T on S.category=T.category