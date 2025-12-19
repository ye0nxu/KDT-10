# function.py
import pymysql

# ===== 공통 테이블 이름 상수 =====
TABLE_EMP = "employees"      # 사원 정보 테이블
ATT_TABLE = "attendance"     # 근태 테이블
SAL_TABLE = "salary"         # 급여 테이블


def get_connection():
    """
    MySQL DB 커넥션 생성 함수.
    - 항상 DictCursor로 반환해서 컬럼명을 키로 사용 가능.
    """
    return pymysql.connect(
        host="172.30.1.33",
        user="user2",
        password="user2",
        db="ems",
        cursorclass=pymysql.cursors.DictCursor
    )


# ---------------------------------------------------------
#  직원 목록 조회 (홈 화면용)
# ---------------------------------------------------------
def get_employee_list():
    """
    홈 화면에서 사용하는 직원 전체 목록 조회 함수.
    - 반환: [{emp_id, name, position, department, email, phone}, ...] 또는 None
    """
    try:
        conn = get_connection()
    except Exception as e:
        print("DB 연결 오류:", e)
        return None

    try:
        with conn.cursor() as cur:
            sql = f"""
                SELECT emp_id, name, position, department, email, phone
                FROM {TABLE_EMP}
                ORDER BY emp_id
            """
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
    except Exception as e:
        print("직원 목록 조회 오류:", e)
        return None
    finally:
        try:
            conn.close()
        except:
            pass


# ---------------------------------------------------------
#  사번별 근태 기록 조회
# ---------------------------------------------------------
def get_attendance_by_emp(emp_id: int):
    """
    특정 사원의 근태(attendance) 기록 조회.
    - TIME 타입(check_in, check_out)이 timedelta/None일 수 있어서
      문자열(HH:MM:SS)로 변환하여 함께 반환.
    """
    try:
        conn = get_connection()
    except Exception as e:
        print("DB 연결 오류:", e)
        return None

    try:
        with conn.cursor() as cur:
            sql = f"""
                SELECT att_date, check_in, check_out, status, status_2
                FROM {ATT_TABLE}
                WHERE emp_id = %s
                ORDER BY att_date
            """
            cur.execute(sql, (emp_id,))
            rows = cur.fetchall()

        # check_in / check_out 문자열 필드 추가
        for r in rows:
            r["check_in_str"] = time_to_str(r.get("check_in"))
            r["check_out_str"] = time_to_str(r.get("check_out"))

        return rows
    except Exception as e:
        print("근태 기록 조회 오류:", e)
        return None
    finally:
        try:
            conn.close()
        except:
            pass


def time_to_str(t):
    """
    DB TIME 타입이 파이썬에서 timedelta 또는 time 또는 None 등으로 올 수 있어
    안전하게 "HH:MM:SS" 문자열로 변환하는 함수.
    """
    import datetime as dt

    if t is None:
        return ""
    # timedelta 타입 처리
    if isinstance(t, dt.timedelta):
        total_seconds = int(t.total_seconds())
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    # time 타입 또는 문자열 타입 처리
    try:
        return t.strftime("%H:%M:%S")
    except Exception:
        try:
            # 문자열인 경우
            tt = dt.datetime.strptime(str(t), "%H:%M:%S").time()
            return tt.strftime("%H:%M:%S")
        except Exception:
            return ""


# ---------------------------------------------------------
#  사번 + 연월별 급여(salary) 조회
# ---------------------------------------------------------
def get_salary_for_emp(emp_id: int, year: int, month: int):
    """
    salary 테이블에서 특정 사원(emp_id)의 특정 연/월 급여 정보를 조회.

    반환 형식 (예시)
    ----------------
    {
        "emp_id": 1001,
        "year": 2025,
        "month": 11,
        "national_pension": ...,
        "health_insurance": ...,
        "long_term_care": ...,
        "employment_insurance": ...,
        "income_tax": ...,
        "local_income_tax": ...,
        "net_salary": ...,
        "basic_salary": ...   # ← employees.basic_salary(연봉)을 12로 나눈 "월 기본급"
    }

    ※ 실제 DB의 salary 테이블에는 basic_salary 컬럼이 없기 때문에,
       여기서 employees 테이블을 한 번 더 조회해서 월 기본급을 계산해
       row["basic_salary"]에 채워서 반환합니다.
    """
    try:
        conn = get_connection()
    except Exception as e:
        print("DB 연결 오류:", e)
        return None

    try:
        with conn.cursor() as cur:
            # 1) 직원 연봉 조회 (employees.basic_salary)
            sql_emp = f"""
                SELECT basic_salary
                FROM {TABLE_EMP}
                WHERE emp_id = %s
            """
            cur.execute(sql_emp, (emp_id,))
            emp_row = cur.fetchone()

            monthly_basic = 0
            if emp_row and emp_row.get("basic_salary") is not None:
                monthly_basic = emp_row["basic_salary"] // 12

            # 2) salary 테이블에서 해당 연/월 급여 내역 조회
            sql_sal = f"""
                SELECT
                    emp_id, year, month,
                    national_pension,
                    health_insurance,
                    long_term_care,
                    employment_insurance,
                    income_tax,
                    local_income_tax,
                    net_salary
                FROM {SAL_TABLE}
                WHERE emp_id = %s AND year = %s AND month = %s
            """
            cur.execute(sql_sal, (emp_id, year, month))
            row = cur.fetchone()

            # 급여 데이터가 없으면 빈 dict 반환 (UI에서 처리)
            if not row:
                return {}

            # UI에서 사용하기 편하도록 월 기본급을 필드로 추가
            row["basic_salary"] = monthly_basic

            return row
    except Exception as e:
        print("급여 조회 오류:", e)
        return None
    finally:
        try:
            conn.close()
        except:
            pass
