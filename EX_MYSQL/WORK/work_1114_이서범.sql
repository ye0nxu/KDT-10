/* 04-2 where문으로 조건에 맞는 데이터 조회 */
/* work_1114 이서범 */
## where 절로 특정 값 조회하기

#1
select * from customer where first_name = 'MARIA';

#2
select * from customer where address_id = 200;

#3
select * from customer where address_id < 200;

#4
select * from customer where first_name = 'MARIA';

#5 
select * from customer where first_name < 'MARIA';

#6
select * from payment where payment_date = '2005-07-09 13:24:07';

#7 
select * from payment where payment_date < '2005-07-09';

#8
select * from customer where address_id BETWEEN 5 AND 10;

#9
select * from payment where payment_date BETWEEN '2005-06-17' AND '2005-07-19';

#10
select * from payment where payment_date = '2005-07-08 07:33:56';

#11
select * from customer 
where first_name BETWEEN 'M' and 'O';

#12
select * from customer
where first_name not BETWEEN 'M' and 'O';

#13
select * from city
where city = 'Sunnyvale' and country_id=103;

#14
select * from payment
where payment_date >= '2005-06-01' and payment_date <= '2005-07-05';

#15
select * from customer
where first_name = 'MARIA' or first_name='LINDA';

#16 
select * from customer
where first_name = 'MARIA' or first_name='LINDA' or first_name='NANCY';

#17
select * from customer
where first_name in ('MARIA' ,'LINDA' ,'NANCY');

#18
select * from city
where (country_id = 103 or country_id = 86) and city in ('Cheju', 'Sunnyvale','Dallas');

#19
select * from address
where address2 is null;

#20
select * from address
where address2 is not null;

#21
select * from address
where address2 = '';

