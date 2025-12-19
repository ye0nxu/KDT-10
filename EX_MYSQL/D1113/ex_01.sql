/* Test 데이터베이스 생성 */
create database if not exists TEST;

/* 사용 데이터베이스 선택 */
use TEST;

/* 테이블 생성 */
create table tbl_product(
pid int,
pname varchar(10),
price int );

/*데이터 추가*/
insert into tbl_product
values(1,'ABD',1000); 

insert into tbl_product(pid, pname)	
values(12,'ABC'),
		(13,"good"),
		(23,'ABC');

/* 데이터 조회 */
select * from tbl_product;