# Write your MySQL query statement below
select customer_id
from customer_transactions
group by customer_id having datediff(max(transaction_date),min(transaction_date))>=29 
                        and sum(case when transaction_type ='purchase' then 1 else 0 end)>=3 
                        and (sum(case when transaction_type='refund' then 1 else 0 end)/count(*))*100 <20
order by customer_id