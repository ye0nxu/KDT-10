## ----------------------------------------------
##          데이터분석 패키지 Pandas 
## ----------------------------------------------
## 모듈 로딩 
## ----------------------------------------------
import pandas as pd 

## 기본 정보 출력
print(f'pandas v.{pd.__version__}')

## -----------------------------------------
## 다양한 종류의 데이터 파일 로딩 
## -----------------------------------------
## 데이터 파일들
DATA_FILES=[ '../Data/test.csv', 
             '../Data/test.txt', 
             '../Data/test.json']
print(f'DATA_FILES => {DATA_FILES}')

## -----------------------------------------
## 함수명: pandas.read_파일확장자( 파일경로 )
## -----------------------------------------
## CSV => DataFrame으로 로딩/변환 
dataDF=pd.read_csv(DATA_FILES[0])
print(f'타입 : {type(dataDF)}')
print(f'출력 : \n{ dataDF }')


## TXT => DataFrame으로 로딩 
dataDF=pd.read_table(DATA_FILES[1])
dataDF=pd.read_csv(DATA_FILES[1])
print(f'타입 : {type(dataDF)}')
print(f'출력 : \n{ dataDF }')


## JSON => DataFrame으로 로딩 
dataDF=pd.read_json(DATA_FILES[2])
print(f'타입 : {type(dataDF)}')
print(f'출력 : \n{ dataDF }')