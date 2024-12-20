-- #IMP are important questions

-- 1) Combine Two Tables
Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255))
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255))
Truncate table Person
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen')
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob')
Truncate table Address
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York')
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California')

-- Q) Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
select person.firstName, person.lastName, address.city, address.state from Person person LEFT JOIN Address address on person.personId = address.personId

-- --------------------------------------------------------------------------------------------------------------------------

-- 2)  181. Employees Earning More Than Their Managers
Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int)
Truncate table Employee
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3')
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4')
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', NULL)
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', NULL)

-- Q) Write a solution to find the employees who earn more than their managers.
SELECT name as Employee from Employee e1 where salary > (select salary from Employee e2 where e1.managerId = e2.id )

-- --------------------------------------------------------------------------------------------------------------------------

-- 3) 182. Duplicate Emails
Create table If Not Exists Person (id int, email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'a@b.com')
insert into Person (id, email) values ('2', 'c@d.com')
insert into Person (id, email) values ('3', 'a@b.com')

-- Q) Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
select email from person group by email having count(*) > 1

------------------------------------------------------------------------------------------------------------------------------

-- 4) 183. Customers Who Never Order
Create table If Not Exists Customers (id int, name varchar(255))
Create table If Not Exists Orders (id int, customerId int)
Truncate table Customers
insert into Customers (id, name) values ('1', 'Joe')
insert into Customers (id, name) values ('2', 'Henry')
insert into Customers (id, name) values ('3', 'Sam')
insert into Customers (id, name) values ('4', 'Max')
Truncate table Orders
insert into Orders (id, customerId) values ('1', '3')
insert into Orders (id, customerId) values ('2', '1')

-- Q) Write a solution to find all customers who never order anything.
select cust.name as Customers from Orders ord right join Customers cust on ord.customerId = cust.id where ord.customerId is null

------------------------------------------------------------------------------------------------------------------------------

-- 5) 196. Delete Duplicate Emails
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'john@example.com')
insert into Person (id, email) values ('2', 'bob@example.com')
insert into Person (id, email) values ('3', 'john@example.com')

-- Q) Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
DELETE p1 FROM Person p1, Person p2 WHERE p1.email = p2.email AND p1.id > p2.id

------------------------------------------------------------------------------------------------------------------------------

-- 6) 197. Rising Temperature
Create table If Not Exists Weather (id int, recordDate date, temperature int)
Truncate table Weather
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10')
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25')
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20')
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30')

-- Q) Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
select w1.id as Id from Weather w1 LEFT JOIN Weather w2 ON datediff(w1.recordDate, w2.recordDate) = 1 WHERE w1.temperature > w2.temperature

------------------------------------------------------------------------------------------------------------------------------
-- 7) 511. Game Play Analysis I
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
Truncate table Activity
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6')
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')

-- Q) Write a solution to find the first login date for each player.
SELECT player_id, MIN(event_date) as first_login FROM Activity GROUP BY player_id

------------------------------------------------------------------------------------------------------------------------------
-- 8) 577. Employee Bonus
Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int)
Create table If Not Exists Bonus (empId int, bonus int)
Truncate table Employee
insert into Employee (empId, name, supervisor, salary) values ('3', 'Brad', NULL, '4000')
insert into Employee (empId, name, supervisor, salary) values ('1', 'John', '3', '1000')
insert into Employee (empId, name, supervisor, salary) values ('2', 'Dan', '3', '2000')
insert into Employee (empId, name, supervisor, salary) values ('4', 'Thomas', '3', '4000')
Truncate table Bonus
insert into Bonus (empId, bonus) values ('2', '500')
insert into Bonus (empId, bonus) values ('4', '2000')

-- Q) Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.
select emp.name, b.bonus from Employee emp LEFT JOIN Bonus b ON emp.empId = b.empId WHERE bonus < 1000 OR bonus is Null

------------------------------------------------------------------------------------------------------------------------------
-- 9) 584. Find Customer Referee
Create table If Not Exists Customer (id int, name varchar(25), referee_id int)
Truncate table Customer
insert into Customer (id, name, referee_id) values ('1', 'Will', NULL)
insert into Customer (id, name, referee_id) values ('2', 'Jane', NULL)
insert into Customer (id, name, referee_id) values ('3', 'Alex', '2')
insert into Customer (id, name, referee_id) values ('4', 'Bill', NULL)
insert into Customer (id, name, referee_id) values ('5', 'Zack', '1')
insert into Customer (id, name, referee_id) values ('6', 'Mark', '2')

-- Q) Find the names of the customer that are not referred by the customer with id = 2.
select name from Customer where referee_id  <> 2 or referee_id is null

------------------------------------------------------------------------------------------------------------------------------
-- 10) 585. Investments in 2016
Create Table If Not Exists Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float)
Truncate table Insurance
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('1', '10', '5', '10', '10')
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('2', '20', '20', '20', '20')
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('3', '10', '30', '20', '20')
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('4', '10', '40', '40', '40')

-- Q) Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:
-- have the same tiv_2015 value as one or more other policyholders, and
-- are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).

WITH CTE AS (
    SELECT 
        *,
        COUNT(lat) OVER(PARTITION BY lat, lon) AS CountLatLon,
        COUNT(tiv_2015) OVER(PARTITION BY tiv_2015) AS COUNT_2015
    FROM
        INSURANCE
)
SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM CTE
WHERE 
    CountLatLon = 1
AND
    COUNT_2015 > 1
------------------------------------------------------------------------------------------------------------------------------
-- 11) 586. Customer Placing the Largest Number of Orders
Create table If Not Exists orders (order_number int, customer_number int)
Truncate table orders
insert into orders (order_number, customer_number) values ('1', '1')
insert into orders (order_number, customer_number) values ('2', '2')
insert into orders (order_number, customer_number) values ('3', '3')
insert into orders (order_number, customer_number) values ('4', '3')

-- Q) Write a solution to find the customer_number for the customer who has placed the largest number of orders.
SELECT customer_number FROM ORDERS GROUP BY CUSTOMER_NUMBER ORDER BY COUNT(*) DESC LIMIT 1

------------------------------------------------------------------------------------------------------------------------------
-- 12)#IMP 601. Human Traffic of Stadium
Create table If Not Exists Stadium (id int, visit_date DATE NULL, people int)
Truncate table Stadium
insert into Stadium (id, visit_date, people) values ('1', '2017-01-01', '10')
insert into Stadium (id, visit_date, people) values ('2', '2017-01-02', '109')
insert into Stadium (id, visit_date, people) values ('3', '2017-01-03', '150')
insert into Stadium (id, visit_date, people) values ('4', '2017-01-04', '99')
insert into Stadium (id, visit_date, people) values ('5', '2017-01-05', '145')
insert into Stadium (id, visit_date, people) values ('6', '2017-01-06', '1455')
insert into Stadium (id, visit_date, people) values ('7', '2017-01-07', '199')
insert into Stadium (id, visit_date, people) values ('8', '2017-01-09', '188')

-- Q) Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
-- Return the result table ordered by visit_date in ascending order.
with cte as (select *, 
    id - ROW_NUMBER() OVER(ORDER BY id) as row_group 
from stadium where people >= 100),
cte2 as (
    select *, count(*) over(partition by row_group) as group_count
    from cte
)
select id, visit_date, people from cte2 where group_count >= 3 order by visit_date

------------------------------------------------------------------------------------------------------------------------------
-- 13)#IMP 602. Friend Requests II: Who Has the Most Friends
Create table If Not Exists RequestAccepted (requester_id int not null, accepter_id int null, accept_date date null)
Truncate table RequestAccepted
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03')
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08')
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08')
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09')
-- Q) Write a solution to find the people who have the most friends and the most friends number.
with cte as (select requester_id as id from RequestAccepted
UNION ALL
select accepter_id as id from RequestAccepted)
select id, count(*) as num from cte group by id order by count(*) desc limit 1

------------------------------------------------------------------------------------------------------------------------------

-- 14) 607. Sales Person
Create table If Not Exists SalesPerson (sales_id int, name varchar(255), salary int, commission_rate int, hire_date date)
Create table If Not Exists Company (com_id int, name varchar(255), city varchar(255))
Create table If Not Exists Orders (order_id int, order_date date, com_id int, sales_id int, amount int)
Truncate table SalesPerson
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('1', 'John', '100000', '6', '4/1/2006')
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('2', 'Amy', '12000', '5', '5/1/2010')
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('3', 'Mark', '65000', '12', '12/25/2008')
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('4', 'Pam', '25000', '25', '1/1/2005')
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('5', 'Alex', '5000', '10', '2/3/2007')
Truncate table Company
insert into Company (com_id, name, city) values ('1', 'RED', 'Boston')
insert into Company (com_id, name, city) values ('2', 'ORANGE', 'New York')
insert into Company (com_id, name, city) values ('3', 'YELLOW', 'Boston')
insert into Company (com_id, name, city) values ('4', 'GREEN', 'Austin')
Truncate table Orders
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('1', '1/1/2014', '3', '4', '10000')
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('2', '2/1/2014', '4', '5', '5000')
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('3', '3/1/2014', '1', '1', '50000')
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('4', '4/1/2014', '1', '4', '25000')

-- Q) Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
select sp.name from salesPerson sp where sp.sales_id not in 
(
    select od.sales_id from Orders od
    JOIN Company cp ON od.com_id = cp.com_id
    where cp.name = 'RED'

)
------------------------------------------------------------------------------------------------------------------------------
-- 15) 608. Tree Node
Create table If Not Exists Tree (id int, p_id int)
Truncate table Tree
insert into Tree (id, p_id) values ('1', NULL)
insert into Tree (id, p_id) values ('2', '1')
insert into Tree (id, p_id) values ('3', '1')
insert into Tree (id, p_id) values ('4', '2')
insert into Tree (id, p_id) values ('5', '2')
-- Q) Each node in the tree can be one of three types:
-- "Leaf": if the node is a leaf node.
-- "Root": if the node is the root of the tree.
-- "Inner": If the node is neither a leaf node nor a root node.
-- Write a solution to report the type of each node in the tree.
select id, (case
    when p_id is null then 'Root'
    when id in (select distinct p_id from Tree) then 'Inner'
    else 'Leaf' end) as "Type" from Tree


------------------------------------------------------------------------------------------------------------------------------
-- 3054: Binary Tree Nodes.
-- 
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------


