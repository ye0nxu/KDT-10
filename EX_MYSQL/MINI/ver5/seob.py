# seob.py
import pandas as pd

# ============================================
# 1. 간이세액표 엑셀 불러오기
# ============================================
# - 근로소득 간이세액표를 미리 로딩해두고
#   work_tax()에서 참조해서 근로소득세를 계산함.
TAX_EXCEL_PATH = "./근로소득_간이세액표(조견표).xlsx"

# 엑셀의 6번째 줄(header=5)부터 실제 표가 시작된다고 가정
# "이상", "미만", "Unnamed: 2"(세액) 컬럼만 사용
df = pd.read_excel(
    TAX_EXCEL_PATH,
    header=5,                      # 6번째 줄부터 실제 표 시작
    usecols=["이상", "미만", "Unnamed: 2"],  # 이상, 미만, 세액 컬럼
)

# 불필요한 하단 행 제거 (원본 파일 구조에 맞춰 조정)
df.drop(df.index[646:], axis="index", inplace=True)

# 결측치는 0으로 채우고, 경고가 안 뜨도록 dtype 정리
df = df.fillna(0)
df = df.infer_objects(copy=False)

# 문자열에 들어있는 쉼표 제거 후 숫자로 변환
for col in df.columns:
    df[col] = (
        pd.to_numeric(
            df[col].astype(str).str.replace(",", "", regex=False),
            errors="coerce",
        ).fillna(0)
    )


# ============================================
# 2. 세금/보험 계산 함수
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


def employment_tax(salary: int) -> int:
    """
    고용보험료 계산 함수.
    - salary: 연봉(연간 총액, 직원의 basic_salary)
    - 내부적으로 월급으로 환산 후, 간단한 비율로 고용보험료 계산.
    """
    month_price = salary // 12            # 연봉 → 월급
    no_eat = month_price - 20             # 비과세 제거 (식대)
    return int(no_eat * 9 / 1000)         # 0.9% 정도로 계산



def work_tax(salary: int) -> int:
    """
    간이세액표 기반 근로소득세 계산 함수.
    - salary: 연봉(연간 총액)
    - 월급을 1,000원 단위로 줄인 값으로 세액표를 조회하여 세금 계산.
    """
    month_price = salary // 12
    month_thousand = int(str(int(month_price))[:-3] or "0") # (예: 3,250,000 → 3250)

    # 이상 <= 값 < 미만 범위에 해당하는 행
    tax_info = df[(df["이상"] <= month_thousand) & (month_thousand < df["미만"])]

    if tax_info.empty:
        return 0

    # "Unnamed: 2" 컬럼 값 출력
    return int(tax_info["Unnamed: 2"].values)


def local_tax(salary: int) -> int:
    """
    지방소득세 계산 함수.
    - 근로소득세(work_tax)의 10%를 지방소득세로 간주.
    """
    return int(work_tax(salary) * 0.10)


# ============================================
# 3. 급여 INSERT 실행 함수
# ============================================

def insert_salary_records(cur, year, month):
    """급여 계산 후 salary 테이블에 삽입"""

    # 기존 월급 삭제
    delete_sql = (
        "DELETE FROM salary "
        "WHERE year = %s AND month = %s"
    )
    cur.execute(delete_sql, (year, month))

    # 직원 연봉 가져오기
    select_sql = (
        "SELECT emp_id, basic_salary "
        "FROM employees"
    )
    cur.execute(select_sql)
    employees = cur.fetchall()

    # INSERT 문
    insert_sql = (
        "INSERT INTO salary ("
        "emp_id, year, month, "
        "national_pension, health_insurance, long_term_care, "
        "employment_insurance, income_tax, local_income_tax, net_salary"
        ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )

    for emp in employees:
        emp_id = emp["emp_id"]
        annual_salary = emp["basic_salary"]

        monthly_basic = annual_salary // 12
        national_pension = National_Pension(annual_salary)
        health_insurance = Health_Insurance(annual_salary)
        long_term_care = Long_term_Care_Insurance(annual_salary)
        emp_ins = employment_tax(annual_salary)
        inc_tax = work_tax(annual_salary)
        loc_tax = local_tax(annual_salary)
        net_salary = (
            monthly_basic - national_pension - health_insurance
            - long_term_care - emp_ins - inc_tax - loc_tax
        )

        cur.execute(
            insert_sql,
            (
                emp_id, year, month,
                national_pension, health_insurance, long_term_care,
                emp_ins, inc_tax, loc_tax, net_salary,
            ),
        )

    return len(employees)
