## ===============================================
## Group by 컬럼명1 
## ===============================================
## DB 선택
use MYDB;

-- hometown 값 종류
select DISTINCT hometown from User
ORDER BY hometown;

-- hometown 기준으로 그룹화
select hometown, count(*) "CNT" from User
GROUP BY hometown;

-- 그룹별 행 수
select hometown, count(hometown) from User
GROUP BY hometown;

## ==================================================
## Group by 컬럼명1, 컬럼명2, .. : 여러 개 컬럼으로 그룹화
## ==================================================
-- hometown, gender 그룹화
select hometown, gender from User
GROUP BY hometown, gender
ORDER BY hometown;

-- 그룹별 행 수, gender 정렬
-- 1. 별칭 사용
select hometown, gender as 성별, count(*) '인원수' from User
GROUP BY hometown, gender
ORDER BY 성별;

-- 2. 별칭 사용 X
select hometown, gender, count(hometown) from User
GROUP BY hometown, gender
ORDER BY gender;
HAVING gender = '남';

select name, count(*) 'cnt'
from user
GROUP BY name;

## ==================================================
## Having 조건 : 그룹화 후 그룹들에 대한 필터링
## ==================================================
-- special features로 그룹화 후 그룹이 행 수가 70개 이상인 그룹만 선택
select special_features, count(*) 'CNT' from film
GROUP BY special_features
HAVING cnt>=70;

-- hometown, gender 그룹화 후 성별이 남자인 그룹 데이터만 선택
select hometown, gender from user
GROUP BY hometown, gender
HAVING gender='남';