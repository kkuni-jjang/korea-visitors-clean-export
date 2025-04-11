# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:17:32 2025

@author: KIMMINJI

여러 개의 엑셀 파일을 전처리하여 통합 !!
kto_201001.xlsx ~ kto_202005.xlsx : 125개 파일
    월별 외국인 관광객 통계에 대한 데이터 수집 : 한국관광데이터랩
"""
import pandas as pd

kto_201901 = pd.read_excel('./data/kto_201901.xlsx',
                           header = 1,       # 첫 번째 행 컬럼으로
                           usecols = 'A:G',  # A ~ G까지 읽어들이기
                           skipfooter=4)     # 아래 4줄 건너뛴다.
kto_201901.head()
kto_201901.tail()

### 데이터 전처리 ###
kto_201901.info()
'''
RangeIndex: 67 entries, 0 to 66
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   국적      67 non-null     object
 1   관광      67 non-null     int64 
 2   상용      67 non-null     int64 
 3   공용      67 non-null     int64 
 4   유학/연수   67 non-null     int64 
 5   기타      67 non-null     int64 
 6   계       67 non-null     int64 
dtypes: int64(6), object(1)
# 결측치 없음 
'''
kto_201901.describe()
'''
           관광            상용  ...            기타              계
count      67.000000     67.000000  ...     67.000000      67.000000
mean    11964.716418    683.462687  ...   4115.910448   16998.597015
std     47055.349998   2639.234303  ...  11560.294887   59189.624627
min         0.000000      0.000000  ...      0.000000      13.000000
25%       254.000000     23.500000  ...    161.500000     605.000000
50%       554.000000     47.000000  ...    449.000000    1350.000000
75%      3638.000000    301.000000  ...   1608.000000    7582.000000
max    329131.000000  18238.000000  ...  80916.000000  433045.000000

[8 rows x 6 columns]
'''
# 각 컬럼에서 0인 부분을 필터링 : 4개 컬럼 중 1개라도 0이 있으면
condition = (kto_201901['관광'] == 0) | (kto_201901['상용'] == 0) | (kto_201901['공용'] == 0) | (kto_201901['유학/연수'] == 0)
'''
0     False
1     False
2     False
3     False
4      True
'''
kto_201901[condition]
'''
        국적      관광 상용 공용 유학/연수 기타  계
65    교포소계     0    0   0      0  15526  15526
66      교포       0    0   0      0  15526  15526
#=> 교포소계 / 교포는 기타값이라서
'''
# 날짜 
kto_201901['기준년월'] = '2019-01'
kto_201901.head()
'''
     국적      관광     상용    공용  유학/연수      기타       계     기준년월
0  아시아주  765082     10837  1423  14087           125521  916950    2019-01
1    일본    198805      2233   127   785              4576  206526    2019-01
'''
# 국적 컬럼이 가지고 있는 유일한 값(목록) 살펴보기
kto_201901['국적'].unique()
'''
array(['아시아주', '일본', '대만', '홍콩', '마카오', '태국', '말레이시아', '필리핀', '인도네시아',
       '싱가포르', '미얀마', '베트남', '인도', '스리랑카', '파키스탄', '방글라데시', '캄보디아', '몽골',
       '중국', '이란', '이스라엘', '터키', '우즈베키스탄', '카자흐스탄', 'GCC', '아시아 기타', '미주',
       '미국', '캐나다', '멕시코', '브라질', '미주 기타', '구주', '영국', '독일', '프랑스',...
'''
# 국적 컬럼이 가지고 있는 값들 중에 필요 없는 값들 처리
continents_list = ['아시아주','미주','구주','대양주','아프리카주',
                   '기타대륙','교포소계']

# 대륙 목록에 해당하는 값 제외
# 국적.isin()       *True = 포함 / False = 불포함
condition = (kto_201901.국적.isin(continents_list) == False)
#                 '미국'
#                           False
#                 .                                  True

#                 '아시아주'
#                           True
#                 .                                  False
kto_201901_country = kto_201901[condition]
kto_201901_country['국적'].unique()
'''
array(['일본', '대만', '홍콩', '마카오', '태국', '말레이시아', '필리핀', '인도네시아', '싱가포르',
       '미얀마', '베트남', '인도', '스리랑카', '파키스탄', '방글라데시', '캄보디아', '몽골', '중국',
       '이란', '이스라엘', '터키', '우즈베키스탄', '카자흐스탄', 'GCC', '아시아 기타', '미국',...
'''
kto_201901_country.head()
'''
    국적      관광    상용   공용  유학/연수    기타       계     기준년월
1   일본  198805  2233  127    785  4576  206526  2019-01
2   대만   86393    74   22    180  1285   87954  2019-01

#=> 인덱스가 1부터 시작
'''

# 인덱스 번호 리셋 (0부터 시작하도록)
# reset_index()는 기존의 인덱스를 초기화하고 새로운 인덱스를 생성하는 함수
# drop=True를 설정하면 기존의 인덱스가 완전히 제거되면서 새로운 인덱스가 생성
kto_201901_country_newindex = kto_201901_country.reset_index(drop = True)
'''
          국적      관광    상용    공용  유학/연수     기타       계     기준년월
0         일본  198805  2233   127    785   4576  206526  2019-01
1         대만   86393    74    22    180   1285   87954  2019-01
2         홍콩   34653    59     2     90   1092   35896  2019-01
'''

# 대륙별
continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 + ['아프리카']*2 + ['기타대륙'] + ['교포']

kto_201901_country_newindex['대륙'] = continents

# 관광객비율(%) 컬럼 생성 : .1
# 관광객비율(%) = 관광 / 계 * 100 
# round(관광객비율(%) = 관광 / 계 * 100, 1)
kto_201901_country_newindex['관광객비율(%)'] =                               \
    round(kto_201901_country_newindex['관광']/
          kto_201901_country_newindex['계']*100, 1)
#--------------------------------------------------------------------------------
# 함수로 선언
def create_kto_data(yy, mm):  # 예: 2018, 12
    # 1. 불러올 Excel 파일 경로 지정 (yy, mm 반영)
    file_path = './data/kto_{}{}.xlsx'.format(yy, mm)
    
    # 2. Excel 파일 불러오기
    df = pd.read_excel(file_path, 
                       header=1,       # 첫 번째 행을 컬럼으로 지정
                       usecols='A:G',  # A ~ G 컬럼만 가져오기
                       skipfooter=4)   # 아래 4줄 생략
    
    # 3. "기준년월" 컬럼 추가 (yy-mm 형식)
    df['기준년월'] = '{}-{}'.format(yy, mm)

    # 4. "국적" 컬럼에서 대륙 제거하고 국가만 남기기
    # 대륙 컬럼 생성을 위한 목록
    ignore_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙', '교포소계']
    
    # 대륙 미포함 조건
    condition = (df['국적'].isin(ignore_list) == False)
    df_country = df[condition].reset_index(drop = True)

    # 5. "대륙" 컬럼 추가
    continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 + ['아프리카']*2 + ['기타대륙'] + ['교포']
    df_country['대륙'] = continents

    # 6. "관광객비율(%)" 컬럼 추가
    df_country['관광객비율(%)'] = round(df_country['관광'] / df_country['계'] * 100, 1)

    # 7. "전체비율(%)" 컬럼 추가
    tourist_sum = df_country['관광'].sum()
    df_country['전체비율(%)'] = round(df_country['관광'] / tourist_sum * 100, 1)

    # 8. 결과 반환
    return df_country

#------------------ 여기까지 함수 선언 -----------------------------------------
# 함수 테스트
kto_test = create_kto_data(2018, 12)
kto_test.head()
'''
for yy in range(2010, 2021):    # 2010 ~ 2020   => 2010-01
    for mm in range(1, 13):     # 1 ~ 12
        temp = create_kto_data(str(yy), str(mm).zfill(2))
                                              # zfill(2) : 01,02,03,...이런 형식으로 바꾸기

kto_202005.xlsx
'''
df = pd.DataFrame()

for yy in range(2010, 2021):    
    for mm in range(1, 13):    
        try : 
            temp = create_kto_data(str(yy), str(mm).zfill(2))
            df = pd.concat([df, temp], ignore_index=True)
            
        except :
            pass

df.info()
'''
RangeIndex: 7500 entries, 0 to 7499
Data columns (total 11 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   국적        7500 non-null   object 
 1   관광        7500 non-null   int64  
 2   상용        7500 non-null   int64  
 3   공용        7500 non-null   int64  
 4   유학/연수     7500 non-null   int64  
 5   기타        7500 non-null   int64  
 6   계         7500 non-null   int64  
 7   기준년월      7500 non-null   object 
 8   대륙        7500 non-null   object 
 9   관광객비율(%)  7500 non-null   float64
 10  전체비율(%)   7500 non-null   float64
dtypes: float64(2), int64(6), object(3)
'''
df.to_excel('./files/kto_total.xlsx', index=False)

#-----------------------------------------------------------------------------
# 국적별 관광데이터를 개별 엑셀 파일로 저장하기
# 과제 : aiffall@naver.com 
# [국적별 관광객 데이터] 스위스.xlsx

# total.xlsx 파일 읽어내기
cn = pd.read_excel('./files/kto_total.xlsx')

# 국가 리스트 : cntry_list
cntry_list = list(cn['국적'].unique())

# 개별 파일로 저장
df = pd.DataFrame()

for cntry in cntry_list:
    
    # 국적으로 필터링
    df = cn[cn['국적'] == cntry]
        
    # 정해 놓은 파일명으로 저장
    df.to_excel('./Homework/[국적별 관광객 데이터]{}.xlsx'.format(cntry), index=False)
































