-- ========================================================
-- Subquery : 쿼리 결과값을 활용한 쿼리문
-- ========================================================
use sakila;

-- ========================================================
-- [1] WHERE절 Subquery -> 중첩 서브쿼리. 대부분의 서브쿼리 해당
--     연산자 IN, ANY, ALL, EXISTS 활용
-- ========================================================
-- [다중행결과] ANA, ROSA와 동일한 customer_id 고객정보 추출
-- 연산자 IN : 서브쿼리 결과 다중행 하나씩 확인해서 맞으면 True
select customer_id from customer 
where first_name in ('ROSA', 'ANA');

select * from customer
where customer_id in (
    select customer_id from customer 
    where first_name in ('ROSA', 'ANA')
);

-- 연산자 ANY : 서브쿼리 결과 다중행 중 한개라고 True면 True
select * from customer
where customer_id = ANY (
    select customer_id from customer 
    where first_name in ('ROSA', 'ANA')
);

-- 부등호 사용
select * from customer
where customer_id > ANY (
    select customer_id from customer 
    where first_name in ('ROSA', 'ANA')
);


-- 연산자 EXISTS : 서브쿼리 결과 행이 있으면 True / 없으면 False => 빠름
-- 반환되는 행 존재 여부만 관심. 실제 반환되는 데이터 관심X. 사용X
-- 서브쿼리의 SELECT * 또는 SELECT 1 형식으로 작성한는 경우 대부분j
select * from customer
where EXISTS (
    select 1 from customer          -- 컬럼명이 1인거임 -> 있다면 행이 있는만큼 나옴 (즉, 있다 없다만 보는거임) -> 빠르게 실행하기 위해
    where first_name in ('KANG')
);