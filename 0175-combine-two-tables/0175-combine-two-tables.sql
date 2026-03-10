# Write your MySQL query statement below
/**
personT
personId 기본키
lastName
firstName

addressT
addressId 기본키
personId
city
state
**/

select firstName, lastName, city, state
from person a
left join address b on a.personId = b.personId