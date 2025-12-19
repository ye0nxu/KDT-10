import pymysql
import pandas as pd

# ============================================
# 0. RDBMS 정보
# ============================================
SEVER_IP = '172.30.1.33'
USER_ID = 'user2'
USER_PW = 'user2'
DB_NAME = 'ems'
CHARSET = 'utf8mb4'

# ============================================
# 1. 간이세액표 엑셀 불러오기
# ============================================
df = pd.read_excel(
    './근로소득_간이세액표(조견표).xlsx',
    header=5,
    usecols=['이상', '미만', 'Unnamed: 2']
)

df.drop(df.index[646:], axis='index', inplace=True)
df = df.fillna(0)

# 타입 숫자로 변경
for col in df.columns:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(',', '', regex=False),
        errors='coerce'
    ).fillna(0)


# ============================================
# 2. 4대보험/세금 계산 함수들
# ============================================

## 국민연금(National Pension)
def National_Pension(salary: int) -> int:
    tax_free = 200000
    base = (salary // 12 - tax_free) // 1000 * 1000
    NP = base * 0.045
    return int(NP)


## 건강보험(Health Insurance)
def Health_Insurance(salary: int) -> int:
    tax_free = 200000
    HI = (salary // 12 - tax_free) * 0.03545
    HI = HI // 10 * 10     # 10원 단위 절삭
    return int(HI)


## 장기요양보험(Long-term Care Insurance)
def Long_term_Care_Insurance(salary: int) -> int:
    tax_free = 200000
    LCI = (salary // 12 - tax_free) * 0.004591
    LCI = LCI // 10 * 10   # 10원 단위 절삭
    return int(LCI)


## 고용보험료
def employment_tax(salary: int) -> int:
    month_price = salary // 12
    no_eat = month_price - 20000   # 식대(20만) 제거라고 가정
    if no_eat < 0:
        no_eat = 0
    return int(no_eat * (9 / 1000))    # 0.9%


## 근로소득세
def work_tax(salary: int) -> int:
    month_price = salary // 12
    # 천원 단위로 줄이기 (3200000 -> 3200)
    month_thousand_str = str(int(month_price))[:-3] or "0"
    month_thousand = int(month_thousand_str)

    tax_info = df[(df['이상'] <= month_thousand) & (month_thousand < df['미만'])]
    if tax_info.empty:
        return 0
    return int(tax_info['Unnamed: 2'].values[0])


## 지방소득세
def local_tax(salary: int) -> int:
    work = work_tax(salary)
    return int(work * 0.10)


# ============================================
# 3. 월급 명세 INSERT + 결과 반환 함수
# ============================================
def insert_salary_records(cur, year: int, month: int):
    """
    employees 테이블에서 emp_id, basic_salary(연봉)를 읽어와
    4대보험/세금/실수령액을 계산하고 salary 테이블에 INSERT.
    계산된 결과를 리스트(dict) 형태로 반환.
    """

    # 결과 담을 리스트
    results = []

    # 1) 기존 해당 년/월 급여 삭제
    delete_sql = """
        DELETE FROM salary
        WHERE year = %s AND month = %s
    """
    cur.execute(delete_sql, (year, month))

    # 2) 직원 연봉 가져오기
    select_sql = """
        SELECT emp_id, basic_salary
        FROM employees
    """
    cur.execute(select_sql)
    employees = cur.fetchall()   # [{'emp_id':..., 'basic_salary':...}, ...]

    # 3) INSERT SQL
    insert_sql = """
        INSERT INTO salary (
            emp_id,
            year,
            month,
            basic_salary,
            national_pension,
            health_insurance,
            long_term_care,
            employment_insurance,
            income_tax,
            local_income_tax,
            net_salary
        ) VALUES (
            %s, %s, %s,
            %s,
            %s, %s, %s,
            %s, %s, %s, %s
        )
    """

    # 4) 직원별 계산 & INSERT
    for emp in employees:
        emp_id = emp["emp_id"]
        annual_salary = emp["basic_salary"]   # 연봉

        monthly_basic = annual_salary // 12

        national_pension   = National_Pension(annual_salary)
        health_insurance   = Health_Insurance(annual_salary)
        long_term_care     = Long_term_Care_Insurance(annual_salary)
        employment_ins     = employment_tax(annual_salary)
        income_tax         = work_tax(annual_salary)
        local_income_tax   = local_tax(annual_salary)

        net_salary = (
            monthly_basic
            - national_pension
            - health_insurance
            - long_term_care
            - employment_ins
            - income_tax
            - local_income_tax
        )

        # DB INSERT
        cur.execute(
            insert_sql,
            (
                emp_id,
                year,
                month,
                monthly_basic,
                national_pension,
                health_insurance,
                long_term_care,
                employment_ins,
                income_tax,
                local_income_tax,
                net_salary,
            ),
        )

        # 반환용 결과 저장
        results.append({
            "emp_id": emp_id,
            "monthly_basic": monthly_basic,
            "national_pension": national_pension,
            "health_insurance": health_insurance,
            "long_term_care": long_term_care,
            "employment_insurance": employment_ins,
            "income_tax": income_tax,
            "local_income_tax": local_income_tax,
            "net_salary": net_salary,
        })

    return results
