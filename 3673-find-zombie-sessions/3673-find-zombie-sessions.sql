# Write your MySQL query statement below

/** 세션 지속 시간은 분 이상 30 
클릭 대비 스크롤 비율이 0.02 미만
**/
select session_id, user_id
        , TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) session_duration_minutes
        , sum(case when event_type='scroll' then 1 else 0 end) scroll_count
from app_events
where user_id not in (select user_id from app_events where event_type='purchase')
group by session_id, user_id  having sum(case when event_type='scroll' then 1 else 0 end)>=5
                     and sum(case when event_type='click' then 1 else 0 end)/sum(case when event_type='scroll' then 1 else 0 end) < 0.2
                    and TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) >=30
order by scroll_count desc, session_id