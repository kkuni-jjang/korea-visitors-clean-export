# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:59:20 2025

@author: KIMMINJI

youtube_rank.xlsx 파일 이용한 시각화
"""
import pandas as pd
import matplotlib.pyplot as plt

# 한글을 표기하기 위한 글꼴 변경(윈도우)
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'C:/Windows/Fonts/malgun.ttf'  # Windows: 맑은 고딕 폰트 경로
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)

elif platform.system() == 'Darwin':  # MacOS
    path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'  # Mac: 애플 고딕 폰트
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)

elif platform.system() == 'Linux':  # 리눅스 환경 고려
    path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # 리눅스: 나눔고딕 폰트 (설치 필요)
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
    
    
# youtube_rank.xlsx
df = pd.read_excel('./files/youtube_rank.xlsx')

# 데이터
df.head()
df.tail()

# 구독자수 tn = 0부터 10개만..
df['subscriber'][0:10]
'''
0    9590만
1    8690만
2    7980만
3    7650만
4    6430만
5    6070만
6    4510만
7    3290만
8    3030만
9    3000만
'''

# 만 => 0000 변경
df['subscriber'].str.replace('만', '0000')
'''
0      95900000
1      86900000
2      79800000
3      76500000
# dtype: object
'''
# 새로운 컬럼으로 저장
df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df.info()
'''
RangeIndex: 1000 entries, 0 to 999
Data columns (total 6 columns):
 #   Column               Non-Null Count  Dtype 
---  ------               --------------  ----- 
 0   title                1000 non-null   object
 1   category             1000 non-null   object
 2   subscriber           1000 non-null   object
 3   view                 1000 non-null   object
 4   video                1000 non-null   object
 5   replaced_subscriber  1000 non-null   object  *
 # dtypes: object(6)
'''
# 타입 변경 : astype('')
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
'''
RangeIndex: 1000 entries, 0 to 999
Data columns (total 6 columns):
 #   Column               Non-Null Count  Dtype 
---  ------               --------------  ----- 
 0   title                1000 non-null   object
 1   category             1000 non-null   object
 2   subscriber           1000 non-null   object
 3   view                 1000 non-null   object
 4   video                1000 non-null   object
 5   replaced_subscriber  1000 non-null   int32  ***
dtypes: int32(1), object(5)
'''

#### 구독자 수 => 파이차트 => 채널 ####
# category => 카테고리 갯수 
# replaced_subscriber => 카테고리별로 더하기 
# 구독자 수, 채널 수 피봇 테이블 생성
# 데이터프레임.pivot_table()
# index = 'category'
# values = 'replaced_subscriber'
# aggfunc = ['sum', 'count']
pivot_df = df.pivot_table(index = 'category',
                          values = 'replaced_subscriber',
                          aggfunc = ['sum', 'count'])
'''
                            sum               count
                    replaced_subscriber   replaced_subscriber
category                                           
[BJ/인물/연예인]         238590000                 57
[IT/기술/컴퓨터]         11070000                   6
[TV/방송]                285970000                108
[게임]                   76830000                  45
[교육/강의]              31090000                  18
'''
# 데이터프레임의 컬럼명 변경
pivot_df.columns = ['subscriber_sum', 'category_count']
pivot_df.head()

# 데이터프레임의 인덱스 초기화 : reset_index()
pivot_df = pivot_df.reset_index()
'''
       category(*)     subscriber_sum     category_count
0   [BJ/인물/연예인]       238590000              57
1   [IT/기술/컴퓨터]        11070000               6
2       [TV/방송]          285970000             108
'''

# 데이터프레임을 내림차순 정렬
pivot_df = pivot_df.sort_values(by = 'subscriber_sum', ascending = False)

plt.figure(figsize=(30,10))

# 카테고리별 구독자수 시각화
plt.pie(pivot_df['subscriber_sum'],
        labels=pivot_df['category'],
        autopct='%1.1f%%')
plt.show()

# 카테고리별 채널 수 시각화 
pivot_df = pivot_df.sort_values(by = 'category_count', ascending = False)

plt.pie(pivot_df['category_count'],
        labels=pivot_df['category'],
        autopct='%1.1f%%')
plt.show()



























































