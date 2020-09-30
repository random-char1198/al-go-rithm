
SELECT max(salary) AS SecondHighestSalary 
FROM employee 
WHERE salary < (SELECT max(salary) FROM employee)
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- #176
-- Inner query will be executed first, therefore
-- $300 will be returned. Outer query will also return highest salary but it will be less than the inner loop.
-- SO $200 will be returned


