select M.name
from Employee E
inner join Employee M on E.managerId = M.id
group by M.name having count(*)>=5