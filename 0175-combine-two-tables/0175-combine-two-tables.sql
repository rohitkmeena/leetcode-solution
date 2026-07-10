# Write your MySQL query statement below
SELECT 
p.firstName,
p.lastName,
a.state,
a.city
FROM Person p
left JOIN Address a
on p.personId = a.personId;