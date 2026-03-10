# Write your MySQL query statement below
/**
이메일 같은거 비교해서 중복된거 있으면 id가 더 큰행 삭제
**/
DELETE p1 FROM Person p1
JOIN Person p2 
ON p1.email = p2.email AND p1.id > p2.id;