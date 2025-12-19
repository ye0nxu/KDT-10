# ## ----------------------------------------------------------
# ## PANDAS WORK - WORK_1020_이준기
# ## ----------------------------------------------------------
# import pandas as pd

# ## ----------------------------------------------------------
# ## 문제 1. 데이터를 시리즈 객체로 저장하기
# ## ----------------------------------------------------------
# # dataSR1 = pd.Series(['점수',100,200,300])
# # print(dataSR1)

# ## 다른 방법
# dataSR1 = pd.Series([100,200,300], name='점수')
# print(dataSR1)

# ## ----------------------------------------------------------
# ## 문제 2. 데이터를 시리즈 객체로 저장하기
# ## ----------------------------------------------------------
# # name = ['인덱스','철수', '영희', '아름']
# # dataSR2 = pd.Series(name,dataSR1)
# # print(dataSR2)

# ## 다른 방법
# data = ['철수', '영희', '아름']
# dataSR2 = pd.Series([100,200,300], 
#                     ['철수', '영희', '아름'], 
#                     name='점수',
#                     dtype='int16')
# print(dataSR2)

# ## ----------------------------------------------------------
# ## 문제 3. 데이터를 시리즈 객체로 저장하기
# ##         저장 후 인덱스 속성과 형태 속성을 출력
# ## ----------------------------------------------------------
# jong_mok = ['종목명', '삼성전자', '셀트리온', '카카오', '삼성전자우', '현대바이오']
# e_price = ['종가', 73000, 356000, 367000, 68600, 34150]
# dataSR3 = pd.Series(e_price, jong_mok)
# print(dataSR3)
# print(f'인덱스 속성 : {dataSR3.index}')
# print(f'형  태 속성 : {dataSR3.shape}')


# ## ----------------------------------------------------------
# ## 문제 4. 파일을 읽어 DataFrame으로 저장하는 함수 적기
# ## ----------------------------------------------------------
# # DATA_datas = ['../Data/data.xlsx',
# #               '../Data/data.csv',
# #               '../Data/data.json']

# # xlsxDF = pd.read_excel(DATA_datas[0])
# # csvDF = pd.read_csv(DATA_datas[1])
# # jsonDF = pd.read_json(DATA_datas[2])



# ## ----------------------------------------------------------
# ## 문제 5. 파일을 읽어 DataFrame으로 저장하기
# ## ----------------------------------------------------------
# data = [
#     ['김은수', 35, '과장'],
#     ['박정민', 30, '대리'],
#     ['이하나', 28, '대리']
#     ]
# cols = ['이름', '나이', '직책']
# dataDF = pd.DataFrame(data, columns=cols)
# print(dataDF)



# ## ----------------------------------------------------------
# ## 문제 6. 아래 데이터를 저장 후 조건을 만족하는 코드 작성하기
# ## ----------------------------------------------------------
# data = [
#     ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
#     ["해운", "팬오션", 21.23, 0.95],
#     ["시스템반도체", "티엘아이", 35.97, 1.12],
#     ["해운", "HMM", 21.52, 3.20],
#     ["시스템반도체", "아이에이", 37.32, 3.55],
#     ["2차전지(생산)", "LG화학", 83.06, 3.75]
#     ]
# columns = ["테마", "종목명", "PER", "PBR"]

# # 6-1 DataFrame으로 저장
# dataDF1 = pd.DataFrame(data,columns=columns)
# print(dataDF1)

# # 6-2 행인덱스를 SK, PO, TL, HMM, IA, LG로 설정해서 저장해 주세요.
# idx = ['SK', 'PO', 'TL', 'HMM', 'IA', 'LG']
# dataDF2 = pd.DataFrame(data,index=idx, columns=columns)

# # 6-3 데이터 전체를 출력하세요.
# print(f'전체 데이터 :\n{dataDF2}')

# # 6-4 행 인덱스 속성만 출력하세요.
# print(f'행 인덱스 속성 : {dataDF2.index}')

# # 6-5 형태 및 차원 정보 출력하세요.
# print(f'형  태 : {dataDF2.shape}')
# print(f'차  원 : {dataDF2.ndim}차원')

# # 6-6 컬럼 속성만 출력하세요.
# print(f'컬럼 속성 : {dataDF2.columns}')

# # 6-7 실제 메모리에 저장된 데이터만 출력해 주세요.
# print(f'실제 데이터 : \n{dataDF2.values}')


################################################################
## 강사님 풀이
## ----------------------------------------------------------
## PANDAS WORK - WORK_1020_이준기
## ----------------------------------------------------------
import pandas as pd

## ----------------------------------------------------------
## 문제 1. 데이터를 시리즈 객체로 저장하기
## ----------------------------------------------------------
dataSR = pd.Series([100,200,300], name='점수')
print('[문제1]---------------------')
print(f'인덱스 : {dataSR.index}')
print(f'이  름 : {dataSR.name}')
print(f'형  태 : {dataSR.shape}')
print(f'차  원 : {dataSR.ndim}차원')
print(f'메모리 : {dataSR.values}')
print(f'타  입 : {dataSR.dtype}')
print(dataSR)


## ----------------------------------------------------------
## 문제 2. 데이터를 시리즈 객체로 저장하기
## ----------------------------------------------------------
data = ['철수', '영희', '아름']
dataSR = pd.Series([100,200,300], 
                    ['철수', '영희', '아름'], 
                    name='점수',
                    dtype='int16')
print('\n[문제2]---------------------')
print(f'인덱스 : {dataSR.index}')
print(f'이  름 : {dataSR.name}')
print(f'형  태 : {dataSR.shape}')
print(f'차  원 : {dataSR.ndim}차원')
print(f'메모리 : {dataSR.values}')
print(f'타  입 : {dataSR.dtype}')
print(dataSR)

## ----------------------------------------------------------
## 문제 3. 데이터를 시리즈 객체로 저장하기
##         저장 후 인덱스 속성과 형태 속성을 출력
## ----------------------------------------------------------
dataSR = pd.Series([73000, 356000, 367000, 68600, 34150], 
                    ['삼성전자', '셀트리온', '카카오', '삼성전자우', '현대바이오'],
                    name = '종가')

print('\n[문제3]---------------------')
print(f'인덱스 : {dataSR.index}')
print(f'이  름 : {dataSR.name}')
print(f'형  태 : {dataSR.shape}')
print(f'차  원 : {dataSR.ndim}차원')
print(f'메모리 : {dataSR.values}')
print(f'타  입 : {dataSR.dtype}')
print(dataSR)


# ## ----------------------------------------------------------
# ## 문제 4. 파일을 읽어 DataFrame으로 저장하는 함수 적기
# ## ----------------------------------------------------------
# DATA_datas = ['../Data/data.xlsx',
#               '../Data/data.csv',
#               '../Data/data.json']

# xlsxDF = pd.read_excel(DATA_datas[0])
# csvDF = pd.read_csv(DATA_datas[1])
# jsonDF = pd.read_json(DATA_datas[2])



## ----------------------------------------------------------
## 문제 5. 파일을 읽어 DataFrame으로 저장하기
## ----------------------------------------------------------
## [5-1] List 타입의 데이터 저장
data_list=[
        ['김은수', 35, '과장'],
        ['박정민', 30, '대리'],
        ['이하나', 28, '대리']
        ]
cols = ['이름', '나이', '직책']
dataDF = pd.DataFrame(data_list, columns=cols)

print('\n[문제5-1]---------------------')
print(f'인덱스 : {dataDF.index}')
print(f'컬럼즈 : {dataDF.columns}')
print(f'형  태 : {dataDF.shape}')
print(f'차  원 : {dataDF.ndim}차원')
print(f'메모리 : \n{dataDF.values}')
print(f'타  입 : {dataDF.dtypes}')
print(dataDF)


## [5-2] Dict 타입의 데이터 저장
##       key => Colum Name으로 설정
data_list={'이름' : ['김은수','박정민','이하나'],
            '나이' : [35, 30, 28],
            '직책' : ['과장','대리','대리']}
dataDF = pd.DataFrame(data_list)

print('\n[문제5-2]---------------------')
print(f'인덱스 : {dataDF.index}')
print(f'컬럼즈 : {dataDF.columns}')
print(f'형  태 : {dataDF.shape}')
print(f'차  원 : {dataDF.ndim}차원')
print(f'메모리 : \n{dataDF.values}')
print(f'타  입 : {dataDF.dtypes}')
print(dataDF)

## ----------------------------------------------------------
## 문제 6. 아래 데이터를 저장 후 조건을 만족하는 코드 작성하기
## ----------------------------------------------------------
data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
    ]
columns_ = ["테마", "종목명", "PER", "PBR"]

# 6-1 DataFrame으로 저장
dataDF1 = pd.DataFrame(data,columns=columns_)
print(dataDF1)

# 6-2 행인덱스를 SK, PO, TL, HMM, IA, LG로 설정해서 저장해 주세요.
idx = ['SK', 'PO', 'TL', 'HMM', 'IA', 'LG']
dataDF2 = pd.DataFrame(data,index=idx, columns=columns_)

# 6-3 데이터 전체를 출력하세요.
print(f'전체 데이터 :\n{dataDF2}')

# 6-4 행 인덱스 속성만 출력하세요.
print(f'행 인덱스 속성 : {dataDF2.index}')

# 6-5 형태 및 차원 정보 출력하세요.
print(f'형  태 : {dataDF2.shape}')
print(f'차  원 : {dataDF2.ndim}차원')

# 6-6 컬럼 속성만 출력하세요.
print(f'컬럼 속성 : {dataDF2.columns}')

# 6-7 실제 메모리에 저장된 데이터만 출력해 주세요.
print(f'실제 데이터 : \n{dataDF2.values}')
