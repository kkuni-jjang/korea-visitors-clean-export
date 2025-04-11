# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:16:55 2025

@author: KIMMINJI
melon.xlsx / genie.xlsx / bugs.xlsx 통합
"""
# 크롤링 결과가 담긴 멜룬, 벅스, 지니 크롤링 엑셀 파이 ㄹ통합
import pandas as pd

excel_names = ['./files/melon.xlsx',
               './files/genie.xlsx',
               './files/bugs.xlsx']

appended_data = pd.DataFrame() # 통합할 텅빈 데이터프레임

for name in excel_names:
    pd_data = pd.read_excel(name)   # 읽기
    
    appended_data = pd.concat([appended_data, pd_data],  # concat : 데이터프레임끼리 연결
                              ignore_index=True)         # 인덱스는 무시
appended_data.info()
'''
RangeIndex: 300 entries, 0 to 299
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   서비스     300 non-null    object
 1   순위      300 non-null    int64 
 2   타이들     300 non-null    object
 3   가수      300 non-null    object
dtypes: int64(1), object(3)
'''

appended_data.to_excel('./files/total.xlsx', index = False)
'''
appended_data = appended_data.append(pd_data) <= ERROR 
*데이터프레임에서 append가 폐지됨  / concat으로 대체 !!
'''

