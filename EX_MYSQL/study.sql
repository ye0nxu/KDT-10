-- Active: 1763095418220@@127.0.0.1@3306@sakila

------------- 03
-- DoItSQL 데이터베이스 생성
CREATE DATABASE DoItSQL;

-- 데이터 베이스 삭제
DROP DATABASE IF EXISTS doitSQL;

-- 데이터 베이스 선택
use doitSQL;

-- doit_create_table 테이블 생성
CREATE TABLE doit_create_table(
    col_1 INT,
    col_2 VARCHAR(50),
    col_3 DATETIME
);
SELECT * FROM doit_create_table;

-- 테이블 삭제하기
DROP Table doit_create_table;

-- 테이블에 데이터 삽입하기
INSERT INTO doit_create_table (col_1, col_2, col_3) VALUES (1, '이서범', '2025-11-19')
INSERT INTO doit_create_table VALUES (1, '이서범', '2025-11-19')

SELECT * FROM doit_create_table;

-- 테이블에 여러 데이터 삽입하기
INSERT INTO doit_create_table VALUES (2, '이서범', '2025-11-19'), (3, '이서범', '2025-11-19'), (4, '이서범', '2025-11-19');
SELECT * FROM doit_create_table;

-- 데이터 수정하기
UPDATE doit_create_table SET col_2 = '김수연'
WHERE col_1 = 1;

SELECT * FROM doit_create_table;

-- col_1 전체에 10 더하기
UPDATE doit_create_table SET col_1 = col_1 + 10;
SELECT * FROM doit_create_table;

-- col_1에서 12인 값 삭제
DELETE FROM doit_create_table 
where col_1 = 12;
SELECT * FROM doit_create_table;

-- 전체 데이터 삭제
DELETE FROM doit_create_table;
SELECT * FROM doit_create_table;

-- 03 되새김 문제
-- Q1 주석달기
/**/ 
--
#

-- Q2 doit_exam 데이터 베이스 생성
CREATE DATABASE doit_exam;

-- Q3 doit_exam_t1 테이블 생성
use doit_exam;
CREATE Table doit_exam_t1(
    Id INT,
    name VARCHAR(50),
    create_date DATETIME
);
INSERT INTO doit_exam_t1 VALUES (1, '강성욱', '2023-10-01 12:22:00'),(2, '이지스퍼블리싱', '2023-10-01 12:22:00'),(3, 'dotimysql', '2023-10-01 12:22:00');
SELECT * FROM doit_exam_t1;

-- Q4 
UPDATE doit_exam_t1 SET name = '출판사'
WHERE Id = 1;

-- Q5
DELETE FROM doit_exam_t1
where Id = 1;

-- Q6
DROP Table doit_exam_t1;

-- Q7
DROP DATABASE doit_exam;

-- Active: 1763095418220@@127.0.0.1@3306@sakila

------------------------ 04 -----------
use sakila;
SELECT FIRST_NAME FROM customer;

SELECT FIRST_NAME, last_name FROM customer;

SELECT * FROM customer;

-- 테이블에 있는 열 조회
show COLUMNS from customer;

SELECT * from customer
where address_id BETWEEN 5 and 10;

-- customer에서 first_name을 기준으로 정렬
SELECT * FROM customer
ORDER BY first_name;

SELECT * FROM customer
ORDER BY store_id, first_name;

SELECT * FROM customer
ORDER BY first_name DESC;

SELECT * FROM customer
ORDER BY store_id ASC, first_name DESC;

-- 상위 10개 데이터 조회하기
SELECT * FROM customer
LIMIT 10;

-- 101번째부터 10개 데이터 조회하기
SELECT * FROM customer
LIMIT 100,10;

-- 100개 건너뛰고 10개 조회
SELECT * FROM customer
ORDER BY customer_id
LIMIT 10 OFFSET 100;

SELECT * FROM customer
WHERE first_name LIKE 'A%'

-- group by
use sakila;
SELECT special_features FROM film
GROUP BY special_features;

SELECT special_features, rating FROM film
GROUP BY special_features, rating;

SELECT special_features, count(*) FROM film
GROUP BY special_features

-- groupby는 select한 열을 반드시 들고와야한다.
SELECT special_features, rating from film
GROUP BY special_features, rating
HAVING rating = 'G';

SELECT special_features, count(*) as cnt from film
GROUP BY special_features
HAVING cnt > 70;

-- 중복 제거하기
SELECT DISTINCT special_features, rating from film;

-- 4-6
-- 자동 증가 table 생성
CREATE Table doit_increment(
    col_1 INT AUTO_INCREMENT PRIMARY KEY,
    col_2 VARCHAR(50),
    col_3 INT
);

SELECT * from doit_increment;
INSERT INTO doit_increment(col_2, col_3) VALUES ('수연',3);
INSERT INTO doit_increment(col_2, col_3) VALUES ('서범',0);

-- 10부터 시작하는거
ALTER TABLE doit_increment AUTO_INCREMENT = 10;

-- auto_increment로 생성한 마지막 행의 값 조회
SELECT LAST_INSERT_ID();

-- 증가값 변경하기
SET @@AUTO_INCREMENT_INCREMENT = 5;
INSERT INTO doit_increment (col_2, col_3) VALUES ('뭉치', 4);
INSERT INTO doit_increment (col_2, col_3) VALUES ('망치', 0);

-- 4장 되새김 문제
-- Q1
use world;
select * from country
where code = 'KOR';

-- Q2
SELECT * FROM country
where region LIKE '%Asia%';

-- Q3
SELECT * FROM country
WHERE length(Name) = 5;

-- Q4
SELECT * FROM country
ORDER BY Population DESC;

-- Q5
SELECT * FROM country
WHERE LifeExpectancy BETWEEN  60 AND 70;

-- Q6
SELECT * FROM country
WHERE (Region not LIKE '%Asia%') and (name LIKE '%g%' or name LIKE '%u%');


SELECT * FROM country
WHERE (Region not LIKE '%Asia%') and (name REGEXP '[g,u]')
ORDER BY Population DESC;

-- Q7
