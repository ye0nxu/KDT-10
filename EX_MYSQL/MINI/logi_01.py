import pandas as pd

df = pd.read_excel('./근로소득_간이세액표(조견표).xlsx',header=5, usecols=['이상','미만','Unnamed: 2'])
df.drop(df.index[646:],axis='index',inplace=True)
df = df.fillna(0)
## 타입 숫자로 변경
for col in df.columns:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '', regex=False), errors='coerce').fillna(0)

## 급여 받아오면 1000원단위까지만 살리기

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


salary = 50000000
print(employment_tax(salary))
print(work_tax(salary))
print(local_tax(salary))