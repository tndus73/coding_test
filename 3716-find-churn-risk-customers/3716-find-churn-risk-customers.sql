# Write your MySQL query statement below
/**계획 수익은50% 과거 최대 수익 보다 낮습니다 .
최소 며칠 동안 구독자였습니다 60**/
with total
as
(
select user_id, event_date, plan_name, monthly_amount 
        , max(monthly_amount) over(partition by user_id) max_historical_amount
        , row_number() over(partition by user_id order by event_date desc) rn
        , row_number() over(partition by user_id order by event_date) rnfirst
from subscription_events
where user_id in (select distinct user_id from subscription_events where event_type='downgrade') 
)
select A.user_id, A.plan_name current_plan, A.monthly_amount current_monthly_amount
        , A.max_historical_amount
        , datediff(A.event_date, B.event_date) days_as_subscriber
from total A
inner join total B on A.user_id=B.user_id
where 1=1
and A.rn=1 and B.rnfirst=1 
and A.plan_name is not null
and datediff(A.event_date, B.event_date) >= 60
and A.monthly_amount < A.max_historical_amount*0.5
order by days_as_subscriber desc, user_id


