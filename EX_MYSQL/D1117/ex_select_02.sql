## =============================================================
## 그룹화 : Group by 그룹화_기준_컬럼명
##         select 절에 집계함수 사용 : max()/min()/sum()/mean()..
## =============================================================
## DB 선택
use sakila;

--TB 선택 & 상세 설명 : desc/describe   TB_NAME
desc film;

## ==============================================================
## GROUP BY 컬럼명1, 컬럼명2, .. : 여러 개 컬럼으로 그룹화
## ==============================================================
-- special features 값 종류
select count(DISTINCT special_features) from film; -- 중복제거하고 확인하니, 값 종류를 확인할 수 있음 + count쓰면 종류 개수도 확인할 수 있음

-- special feature 기준으로 그룹화
select special_features
from film
GROUP BY special_features;


-- 그룹별 행 수
select special_features, count(special_features) 
from film
GROUP BY special_features;


## ==============================================================
## GROUP BY 컬럼명1, 컬럼명2, .. : 여러 개 컬럼으로 그룹화
## ==============================================================
-- special_features, rating
select distinct rating
from film;

-- special_features, rating 그룹화
select special_features, rating
from film
GROUP BY special_features, rating;

-- special_features, rating 그룹별 행수
select special_features, rating, count(rating) as 'rating 개수'
from film
GROUP BY special_features, rating;

-- rating, special_features 그룹화
select special_features, rating, count(rating) as 'rating 개수'
from film
GROUP BY rating, special_features ;

## ==============================================================
## count() 집계함수와 정렬 order by
## ==============================================================
-- special features 그룹별 소속된 행 개수 파악
select special_features, count(special_features) 'CNT' -- 별칭 설정 
from film
GROUP BY special_features;

-- special features 그룹별 소속된 행 개수 파악
select special_features, count(special_features) 'CNT' -- 별칭 설정 
from film
GROUP BY special_features
ORDER BY cnt desc, special_features desc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           -- cnt(별칭)가 똑같은 값일 떄, 이름으로 정렬 
LIMIT 5;

