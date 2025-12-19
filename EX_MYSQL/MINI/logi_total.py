import pandas as pd

## RDBMS 정보
SEVER_IP = '172.30.1.33'
USER_ID = 'user2'
USER_PW = 'user2'
DB_NAME = 'ems'
CHARSET = 'utf8mb4'

df = pd.read_excel('./근로소득_간이세액표(조견표).xlsx',header=5, usecols=['이상','미만','Unnamed: 2'])
df.drop(df.index[646:],axis='index',inplace=True)
df = df.fillna(0)
for col in df.columns: ## 타입 숫자로 변경
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '', regex=False), errors='coerce').fillna(0)


## 국민연금(National Pension)
def National_Pension(salary):
        tax_free = 200000
        salary = (salary//12  - tax_free)//1000 * 1000
        NP = salary * 0.045
        return NP 


## 건강보험(Health Insurance)
def Health_Insurance(salary):
    tax_free = 200000
    HI = (salary//12  - tax_free) * 0.03545
    HI = HI // 10 * 10
    return HI


## 장기요양보험료(Long-term Care Insurance)
def Long_term_Care_Insurance(salary):
    tax_free = 200000
    LCI = (salary//12  - tax_free) * 0.004591
    LCI = LCI // 10 * 10
    return LCI


## 고용보험료
def employment_tax(salary):
    month_price = salary // 12
    no_eat = month_price - 20 ## 식대 제거
    print('------ 고용보험료 출력 ------')
    return int(no_eat * (9/1000))


## 근로소득세
def work_tax(salary):
    month_price = salary // 12
    month_price = int(str(month_price)[:-3])
    tax_info = df[(df['이상'] <= month_price) & (month_price < df['미만'])]
    print('------ 근로소득세 출력 ------')
    return int(tax_info['Unnamed: 2'].values[0])


## 지방소득세
def local_tax(salary):
    work = work_tax(salary)
    print('------ 지방소득세 출력 ------')
    return int(work * (10/100))


