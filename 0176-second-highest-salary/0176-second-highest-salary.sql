# Write your MySQL query statement below
SELECT(
    Select distinct Salary 
    from Employee
    order by salary Desc
    limit 1 offset 1
) AS SecondHighestSalary ;