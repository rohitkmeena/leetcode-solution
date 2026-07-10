# Write your MySQL query statement below
Select name As Customers
From Customers
where id Not IN (
    Select customerId
    From Orders
);
