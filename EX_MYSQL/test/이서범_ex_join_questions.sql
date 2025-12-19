-- ===========================================================
-- 1. JOIN 문제 (J1 ~ J10)
-- ===========================================================

use employees;

# o
-- ----------------------------------------------------------
-- J1. 직원의 이름과 현재 소속 부서명
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
select first_name, last_name, dept_name FROM employees
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no    -- 직원과 부서 연결
JOIN departments ON dept_emp.dept_no = departments.dept_no  -- 부서 이름 연결
WHERE dept_emp.to_date > '2025-11-20';

# o
-- ----------------------------------------------------------
-- J2. 현재 부서 관리자 정보
-- 테이블: employees.employees, departments,dept_manager
-- ----------------------------------------------------------
SELECT first_name, last_name, dept_name FROM employees
JOIN dept_manager ON employees.emp_no = dept_manager.emp_no -- 관리자 번호 맞는거 연결
JOIN departments ON dept_manager.dept_no = departments.dept_no -- 부서 이름 연결
WHERE dept_manager.to_date > '2025-11-20' AND dept_manager.to_date > '2025-11-20';


# o
-- ----------------------------------------------------------
-- J3. 직원의 현재 직급과 현재 급여
-- 테이블: employees.employees, titles, salaries
-- ----------------------------------------------------------
SELECT first_name, last_name, title, salary FROM employees
JOIN titles ON employees.emp_no = titles.emp_no
JOIN salaries ON titles.emp_no = salaries.emp_no
where titles.to_date > '2025-11-20' AND salaries.to_date > '2025-11-20';


# o
-- ----------------------------------------------------------
-- J4. 부서별 평균 급여 (60,000 이상인 부서만)
-- 테이블: employees.salaries, departments
-- ----------------------------------------------------------
SELECT dept_no, avg(salary) FROM salaries
JOIN dept_emp ON salaries.emp_no = dept_emp.emp_no
WHERE salaries.to_date > '2025-11-20'
GROUP BY dept_no
HAVING avg(salary) >= 60000;

# o
-- ----------------------------------------------------------
-- J5. 'Sales' 부서에 속한 현재 직원 목록
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
SELECT first_name, last_name, dept_name FROM employees
JOIN dept_emp ON employees.emp_no = dept_emp.emp_no
JOIN departments ON dept_emp.dept_no = departments.dept_no
WHERE dept_emp.to_date > '2025-11-20' AND departments.dept_name = 'Sales';


-- ----------------------------------------------------------
-- J6. 같은 부서에 속한 직원 
-- 테이블: employees.employees, departments
-- ----------------------------------------------------------
-- SELECT ;


-- ----------------------------------------------------------
-- J7. 관리자별 담당 부서 직원 수
-- 테이블: employees.dept_manager, employees, departments
-- ----------------------------------------------------------
-- SELECT dept_no, count(*) from dept_manager
-- JOIN 


-- ----------------------------------------------------------
-- J8. 직급 변경 이력이 있는 직원
-- 테이블: employees.employees, titles
-- ----------------------------------------------------------



-- ----------------------------------------------------------
-- J9. 같은 급여를 받는 직원 
-- 테이블: employees.salaries, employees
-- ----------------------------------------------------------
select * from employees
where( 
    select salary from employees
    JOIN salaries ON employees.emp_no = salaries.emp_no
    GROUP BY salary);

-- ----------------------------------------------------------
-- J10. 직원별 최근 급여 이력만 조회
-- 테이블: employees.employees, salaries
-- ----------------------------------------------------------

