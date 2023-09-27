create table customers(
id INT primary key,
name varchar(100),
email varchar(100),
address varchar(100),
phone_number varchar(100)

);
-- drop table customers;
insert into customers value(1,"shyam","shyam@123gmail.com","new delhi",9598839695);

-- select * from customers

-- select name,email from customers

-- SQL
-- INSERT INTO Customers (id, name, email, address, phone_number)
-- VALUES
--     (2, 'Jane Smith', 'jane.smith@example.com', '456 Elm St', '555-987-6543'),
--     (3, 'Alice Johnson', 'alice.johnson@example.com', '789 Oak St', '555-234-5678'),
--     (4, 'Bob Brown', 'bob.brown@example.com', '101 Pine St', '555-876-5432'),
--     (5, 'Eve Davis', 'eve.davis@example.com', '202 Maple St', '555-345-6789');


-- select * from customers where id=3;

select * from customers where name like 'A%';

select * from customers;

select * from customers order by name desc;

update customers set address = 'mrj' where id = 4;

select * from customers;

select * from customers order by id ASC limit 3;

delete from customers where id=2;


select count(*) from customers ;

-- SQL
-- SELECT * FROM Customers ORDER BY id ASC OFFSET 2-- 

SELECT * FROM customers where id > 2 and name like 'B%';

select * from customers where id < 3 or name like '%s';


select * from customers where phone_number is null;



