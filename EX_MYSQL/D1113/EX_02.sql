-- 1줄 주석 기호. 또는 #도 가능
# 1중 주석 기호.

/*
	여러 줄 주석
*/

## ----------------------------------
## Test 데이터베이스에 데이터 추가
## ----------------------------------
## 데이터베이스 선택 : use 데이터베이스이름;
use Test;

## 데이터베이스에 존재하는 테이블 확인 : show tables;
show tables;

## 테이블 구조 확인 : desc 테이블이름;
desc tbl_product;

## 데이터 추가 : (1) 모든 컬럼에 데이터 추가
## - 컬럼 수와 입력 데이터 수 일치
## - 컬럼 순서와 입력 데이터 순서 일치
## insert into 테이블이름 values ( 컬럼별_데이터, 컬럼별_데이터 );
insert into tbl_product values (1, "tv", 1000); -- 1개추가
insert into tbl_product
values (1,'tv',1000), (2,'의자',2580); -- 2개 즉, 여러개 추가

## 데이터 추가 : (2) 일부 컬럼에 데이터 추가
## insert into 테이블이름(컬럼명, 컬럼명) values (컬럼별_데이터, 컬럼별_데이터);
insert into tbl_product(pid, price) values (20,5900);
insert into tbl_product(pid, price) values (20,5900), (21,10101), (29,8769);

## => price 필드/컬럼 제약조건 : not null 즉, 빈칸 허용하지 않음!! 반드시 데이터 입력
-- insert into tbl_product(pid, pname) values (30, "bag"); -- ERROR 발생
insert into tbl_product(price) values (9990);

## -> 데이터 조회 : (1) 모든 컬럼 조회
## 	  select 조회할 컬럼명 from 테이블이름;
select pid, pname, price from tbl_product;
select * from tbl_product;					-- * 의미 : 테이블에 모든 컬럼

## -> 데이터 조회 : (2) 일부 컬럼 조회
## 	  select 조회할 컬럼명 from 테이블이름;
-- pname 컬럼만 조회 
select pname from tbl_product;

-- pname, price 컬럼만 조회
select pname, price from tbl_product;
