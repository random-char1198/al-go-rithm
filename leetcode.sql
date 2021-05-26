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
SELECT max(salary) AS SecondHighestSalary 
FROM employee 
WHERE salary < (SELECT max(salary) FROM employee)



--182
--remove duplicates
create table Test(id integer, email varchar(100));
insert into Test(id, email) values(4, "test1@outlook.com");
insert into Test(id, email) values(2, "test2@gmail.com");
insert into Test(id, email) values(3, "test2@gmail.com");
-- Test1
select email
from Test
group by email
-- will return 
--email
--dongpei1198@outlook.com
--dongpei1198@gmail.com

select email from student
group by email
having count(email)>1
-- will return any entries that is more than 1.
--email
--dongpei1198@gmail.com

