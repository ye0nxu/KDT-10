## ===============================================
## 조회 개수 제한 / 중복 제거 / 정렬
## ===============================================
## DB 선택
use sakila;

## ==============================================================
## 조회 결과 개수 제한 : limit 숫자 => 0부터 ~ 숫자 개수
##                     limit 첫번째부터 몇개 건너뛸 개수, 조회 개수
## ==============================================================
## 5개 데이터만 조회
select * from customer;

-- head() 같은 느낌임
select * from customer limit 5;  

-- 5개 건너뛰고 3개
select * from customer limit 5, 3;

-- 5개 건너뛰고 3개 : limit 추출개수 offset 건너뛸 개수
select * from customer limit 3 OFFSET 5;

## ==============================================================
## 중복 제거 : distinct 컬럼명
## ==============================================================
select store_id from customer;

-- 중복 제거하고 store_id 안에 있는걸 보여줘
select distinct store_id from customer;

-- count() : 개수 반환
select count(store_id) as store_id_count from customer;

-- 중복 제거하고 몇개 있는가?
select count(distinct store_id) from customer;

## ==============================================================
## 정렬 : order by 정렬기준 컬럼명 ASC[기]/DESC 
##       limit 숫자
## ==============================================================
-- asc 하고 limit 하면 상위 5개 / desc 하고 limit 하면 하위 5개 
-- Top-N개 : limit와 함께 조회 / 정렬 조건에 따라 상위.하위
select first_name from customer
where customer_id >= 100
ORDER BY first_name desc
limit 5; 


select customer_id, first_name, last_name  from customer
ORDER BY customer_id desc 
limit 3;