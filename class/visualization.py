# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:06:50 2025

@author: KIMMINJI
"""
import pandas as pd

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

import matplotlib.pyplot as plt

df = pd.read_excel('./kto/kto_total.xlsx')

### 중국인 관광객 시계열 ###
# 1. 중국 국적 데이터 필터링  => df_fitter
condition = (df['국적'] == '중국')
df_fitter = df[condition]

# 2. 시계열 : plot(x, y)
plt.plot(df_fitter['기준년월'], df_fitter['관광'])
plt.show()

# 3. 시계열 : 그래프 크기 조절 / 타이틀, x축, y축 이름 / x 축 눈금 값
# 그래프 크기 조절 :figure() => figsize = ( , )
plt.figure(figsize= (14,4))

# 그래프 데이터 설정
plt.plot(df_fitter['기준년월'], df_fitter['관광'])

# 타이틀 : title()
plt.title('중국 국적의 관광객 추이')
# x축 : xlabel()
plt.xlabel
# y축 : ylabel()
plt.ylabel('관광객수')
# x 축 눈금 : xticks() => [ '2010-01',..., '2020-01']
plt.xticks(['2010-01','2011-01','2012-01','2013-01','2014-01','2015-01','2016-01','2017-01','2018=01','2019-01','2020-01'])
plt.show()


### 국내 외국인 관광객 중 상위 5개 국가를 각각 시계열 ###
### (중국, 일본, 대만, 미국, 홍콩)
# 1. 상위 5개 국가의 리스트
cntry_list = ['중국', '일본', '대만', '미국', '홍콩']

# 2. 위의 시각화 코드를 매번 사용 ? / 반복 처리 / 함수 처리
# 매번, 함수 처리는 여러번 해야해서 귀찮
# 반복 처리 사용
for cntry in cntry_list :
    condition = (df['국적'] == cntry)
    df_fitter = df[condition]
    
    plt.figure(figsize= (14,4))
    # '기준년월'을 datetime 형식으로 변환 (필수)
    df_fitter['기준년월'] = pd.to_datetime(df_fitter['기준년월'])
    xticks_labels = ['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', 
                     '2015-01', '2016-01', '2017-01', '2018-01', '2019-01', '2020-01']
    
    plt.plot(df_fitter['기준년월'], df_fitter['관광'])
    plt.title('{} 국적의 관광객 추이'.format(cntry))
    plt.xlabel('기준년월')
    plt.ylabel('관광객수')
    plt.xticks(pd.to_datetime(xticks_labels), xticks_labels, ha='right')
    plt.show()
    
# 함수 처리 : 관광 / 유학 / 기타
def plot_test(cntry, why):
    """
    특정 국가(`cntry`)의 특정 목적(`why`)에 대한 관광객 수 추이를 시각화하는 함수.

    Parameters:
    - cntry (str): 국가명 (예: '중국', '일본')
    - why (str): 목적 (예: '관광', '유학', '기타')

    Returns:
    - 시계열 그래프 출력
    """
    # '국적'이 cntry인 데이터 필터링
    condition = (df['국적'] == cntry)
    df_fitter = df[condition]
    
    # '기준년월'을 datetime 형식으로 변환 (필수)
    df_fitter['기준년월'] = pd.to_datetime(df_fitter['기준년월'])
    xticks_labels = ['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', 
                     '2015-01', '2016-01', '2017-01', '2018-01', '2019-01', '2020-01']
    plt.figure(figsize=(12, 4))
    plt.plot(df_fitter['기준년월'], df_fitter[why])
    plt.title(f'{cntry} 국적의 {why} 목적 방문객 추이')
    plt.xlabel('기준년월')
    plt.ylabel(f'{why} 방문객 수')  # 목적에 맞게 Y축 라벨 변경

    # X축 눈금 설정 (날짜 변환 및 회전)
    plt.xticks(pd.to_datetime(xticks_labels), xticks_labels, rotation=30, ha='right')
    plt.show()
    
plot_test('중국', '유학/연수')
# plot_test('cntry',why)

### 히트맵 ###
'''
매트릭스 형태에 
값을 컬러로 표현하는 데이터 시각화 방법
장점 : 전체 데이터를 한눈에 파악할 수 있다.

x축, y축에 어떤 변수들을 사용할 지를 고민해야 한다.
'''
# x축 : 월(Month), y축 : 연(Year)
# 데이터 : 관광객 수
#=> 연도와 월로 구분된 변수를 생성 : 기준년월 => 2010-01 str.slice(staridx,endidx)
df['년도'] = df['기준년월'].str.slice(0,4)
df['월'] = df['기준년월'].str.slice(5,7)

# 원하는 국적 데이터만 추출 : df_fitter
condition = (df['국적'] == '중국')
df_fitter = df[condition]

# df_fitter 데이터를 매트릭스 형태로 변환 : pivot_table()
# index = '년도' 
# columns = '월'
# values = '관광'
df_pivot = df_fitter.pivot_table(index = '년도',
                                 columns = '월',
                                 values = '관광')

import seaborn as sns
plt.figure(figsize=(16,10))

sns.heatmap(df_pivot, 
            annot = True,
            fmt = '.0f',
            cmap = 'rocket_r')

plt.title('중국 관광객 히트맵')
plt.show()
































