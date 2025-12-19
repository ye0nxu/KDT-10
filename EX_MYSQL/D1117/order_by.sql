## 4-3 교재
--1
select * from customer 
ORDER BY first_name;  -- 정렬임

--2
select * from customer ORDER BY last_name;

--3
select * from customer ORDER BY store_id, first_name;

--4
select * from customer ORDER BY first_name, store_id;

--5
select * from customer
ORDER BY first_name ASC;

--6
select * from customer
ORDER BY first_name DESC;

--7
select * from customer ORDER BY store_id DESC, first_name ASC;

--8
select * from customer
ORDER BY store_id DESC, first_name ASC
LIMIT 10;

--9
select * from customer 
ORDER BY customer_id ASC
LIMIT 100,10;

--10
select * from customer
ORDER BY customer_id ASC
LIMIT 10 OFFSET 100;

