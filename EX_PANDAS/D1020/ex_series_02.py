## =================================================
## Series 인스턴스/객체 생성 - 다양한 방식
## =================================================
##-> 모듈 로딩
## -------------------------------------------------
import pandas as pd


## -------------------------------------------------
##-> 데이터 준비
## -------------------------------------------------
jumsu=[99, 77, 55, 88, 66]
idx = ['국어','영어','미술','과학','수학']


## -------------------------------------------------
## 함수기능 : Series객체의 속성 출력 기능
## 함수이름 : print_attr
## 매개변수 : sr       - 시리즈 인스턴스/객체
##           sr_name  - 시리즈 인스턴스/객체 이름
## 반환결과 : 없음
## -------------------------------------------------
def print_attr(sr, sr_name):
    print(f'\n---[{sr_name} 속성 읽기]---')
    print(f'인덱스 : {sr.index}')
    print(f'데이터 : {sr.values}, {type(sr.values)}')
    print(f'형  태 : {sr.shape}')     ## 1차원으로 원소 수 반환
    print(f'차  원 : {sr.ndim}차원')   ## 1차원
    print(f'타  입 : {sr.dtype}')  


## -------------------------------------------------
##-> Series로 변환 저장
## -------------------------------------------------
##-> data, index  
dataSR1 = pd.Series(jumsu, idx)
print(dataSR1)

##-> data, index, dtype=pd.Int8Dtype()
dataSR2 = pd.Series(jumsu, idx, dtype=pd.Int8Dtype())
print(dataSR2)

##-> data, index, dtype='int8'
dataSR3 = pd.Series(jumsu, idx, dtype='int8')
print(dataSR3)


##-> data, index, dtype='int8'
dataSR4 = pd.Series(jumsu, idx, dtype='int8', name='jumsu')
print(dataSR4)


## -------------------------------------------------
##-> Series 인스턴스의 속성 읽기
## -------------------------------------------------
## dataSR1 속성 
print_attr(dataSR1, 'dataSR1')    

## dataSR2 속성 
print_attr(dataSR2, 'dataSR2') 

## dataSR3 속성 
print_attr(dataSR3, 'dataSR3') 

## dataSR4 속성 
print_attr(dataSR4, 'dataSR4') 