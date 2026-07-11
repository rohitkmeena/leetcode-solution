# Write your MySQL query statement below
Select e1.name as name 
from Employee e1
join Employee e2
on e2.managerId = e1.id
group by e1.id, e1.name having count(*) >= 5;
