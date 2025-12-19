## =====================================
## 산술연산
## =====================================
## 기본 연산자 : +, -, *, /, div, %, mod
select 5/2,
	   5 div 2 as '몫' ,
	   5 % 2 as '나머지', 5 mod 2 as '나머지' ;
       
## 문자열과 연산자 : '1' => 자동 형변환, 'a' => 0
select 'A'+2 , 'A' * 3 , '1' + 3 ; 

## =====================================
## 논리값과 비교연산
## =====================================
SELECT TRUE, FALSE, true, false;

select TRUE, !TRUE, NOT TRUE;

select 10, !10, not 10;

## =====================================
## 비교연산 :  같다       =, <=>
##		     같지 않다  !=, <>
## =====================================
SELECT 3 = 1, 3 <=> 1, 3 = 3, 3 <= 3 ;

SELECT 3 != 1, 3 <> 1, 3 != 3, 3 <> 3;


## =====================================
## NULL : 없는 것/빈 칸/ 결측치
##	      is null/ is not null
## =====================================
select null is null, null is not null;
select 10 is null, 10 is not null;


## =====================================
## 비교연산 : 범위/구간 비교
##		   between min 	and max	: min<= ~ <=max
##	   not between min 	and max	: < min	   max<
## =====================================
select 3 between 1 and 3;			-- 1<= ~ <= 3
select 3 not between 1 and 3;		-- 3<1   3>3

## =========================================================
## 문자열 일부 부분 비교  : like '00%' 		: 0개 ~ N개 문자
##					   like 'OO_'		: 1개 문자
##					   like '00_ _ _'	: 3개 문자
## =========================================================
select 'abc'    like 'ab%',
	   'abcdef' like 'ab%',
       'ab'	    like 'ab%',
	   'aa'     like 'ab%';

select 'abc'    like 'ab_',
	   'abcdef' like 'ab_',
       'ab'	    like 'ab_',
	   'aa'     like 'ab_';
       
-- ha로 시작하고 문자열 안에 c가 존재하고 글자
select  'hac' 		like 'ha%c%',
		'habbc'		like 'ha%c%',
        'haaaczef'  like 'ha%c%',
        'hhaaczef'  like 'ha%c%';