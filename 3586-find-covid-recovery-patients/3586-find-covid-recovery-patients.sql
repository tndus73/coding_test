# Write your MySQL query statement below
with Positive 
as
(
select patient_id, test_date
from covid_tests
where result ='Positive'
)
,   Negative
as
(
select patient_id, test_date
from covid_tests
where result ='Negative'
)
select P.patient_id, patient_name, age, datediff(min(N.test_date),min(P.test_date)) recovery_time
from  Positive P
inner join Negative N on P.patient_id=N.patient_id and P.test_date < N.test_date
inner join patients C on P.patient_id=C.patient_id
group by P.patient_id, patient_name, age
order by recovery_time, patient_name