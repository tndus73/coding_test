# Write your MySQL query statement below
with firstT
as
(
select driver_id, avg(distance_km / fuel_consumed) half_avg
from trips T1
where month(trip_date) between 1 and 6
group by driver_id
)
,   secondT
as
(
select driver_id, avg(distance_km / fuel_consumed) half_avg
from trips T2
where month(trip_date) between 7 and 12
group by driver_id
)

select T1.driver_id, driver_name, round(T1.half_avg,2) first_half_avg, round(T2.half_avg,2) second_half_avg
        , round(T2.half_avg-T1.half_avg,2) efficiency_improvement
from firstT T1
inner join secondT T2 on T1.driver_id=T2.driver_id
inner join drivers T3 on T1.driver_id=T3.driver_id
where T2.half_avg-T1.half_avg >0
order by efficiency_improvement desc, driver_name

