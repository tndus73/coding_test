select name Customers
from Customers
where id not in (select customerId
                from Orders)
/**
SELECT name AS Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customerId = c.id
);
**/