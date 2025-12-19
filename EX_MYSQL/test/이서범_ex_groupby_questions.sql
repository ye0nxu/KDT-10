-- ===========================================================
-- 1. GROUP BY 문제
-- ===========================================================

use employees;
select * from employees;

# o
-- ----------------------------------------------------------
-- G1. 성별별 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
SELECT gender, count(*) FROM employees
GROUP BY gender;

# o
-- ----------------------------------------------------------
-- G2. 부서별 현재 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
-- 1 : department에 dept_name이 부서임 -> dept_no로 구분됨
-- 2 : dept_emp에 emp_no별 dept_name이 나와있음
SELECT dept_no, count(*) FROM dept_emp
where to_date > '2025-11-20'
GROUP BY dept_no;

# o
-- ----------------------------------------------------------
-- G3.직급별 직원 수 (전체 이력 기준)
-- 테이블: employees.title
-- ----------------------------------------------------------
SELECT * FROM titles;
SELECT title, count(*) FROM titles
GROUP BY title;

# o
-- ----------------------------------------------------------
-- G4. 직급별 “현재” 직원 수 ##
-- 테이블: employees.title
-- ----------------------------------------------------------
SELECT title, count(*) FROM titles
WHERE titles.to_date > '2025-11-20'
GROUP BY title;

# o
-- ----------------------------------------------------------
-- G5.부서별 평균 급여 (현재 기준)
-- 테이블: employees.title
-- ----------------------------------------------------------
select title, avg(salary) FROM titles
JOIN salaries ON titles.emp_no = salaries.emp_no
WHERE titles.to_date > '2025-11-20' AND salaries.to_date > '2025-11-20'
GROUP BY title;


# o
-- ----------------------------------------------------------
-- G6.입사 연도별 직원 수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select hire_date, count(*) FROM employees
GROUP BY hire_date;


# o
-- ----------------------------------------------------------
-- G7.부서별 남녀 인원수
-- 테이블: employees.employees
-- ----------------------------------------------------------
select dept_no, gender, count(*) FROM dept_emp
JOIN employees ON dept_emp.emp_no = employees.emp_no
GROUP BY dept_no, gender;

# 
-- ----------------------------------------------------------
-- G8.부서별 평균 재직 일수
-- 테이블: employees.employees
-- ----------------------------------------------------------
SELECT dept_no, DIFF(dept_emp.to_date, dept_emp.from_date) FROM dept_emp
GROUP BY dept_no;


# o
-- ----------------------------------------------------------
-- G9.직급별 평균 급여 (현재 직급 + 현재 급여)
-- 테이블: employees.employees
-- ----------------------------------------------------------
select title, avg(salary) FROM titles
JOIN salaries ON titles.emp_no = salaries.emp_no
WHERE titles.to_date > '2025-11-20' AND salaries.to_date > '2025-11-20'
GROUP BY title;


#
-- ----------------------------------------------------------
-- G10.부서별 직원 수 + 전체 합계 
-- 테이블: employees.employees
-- ----------------------------------------------------------