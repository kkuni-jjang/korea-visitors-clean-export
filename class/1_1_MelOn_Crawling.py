# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:12:44 2025

@author: KIMMINJI

MelOn_Crawling => Excel 파일로 저장 
"""
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
#------------------------------------------------------------------------------
# 반복문을 이용해 곡과 가수명을 song_data에 저장
song_data = []

rank = 1    # 순위

songs = soup.select('table > tbody > tr')
len(songs)  # 100개

for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > a')[0].text
    
    song_data.append(['Melon', rank, title, singer])
    
    rank += 1
    
song_data[0]    #=> ['Melon', 1, 'REBEL HEART', 'IVE (아이브)']

# song_data 리스트를 이용해 데이터프레임 만들기
import pandas as pd

columns = ['서비스','순위','타이들','가수']   # 컬럼 만들기

pd_data = pd.DataFrame(song_data, columns = columns)    # 데이터프레임
pd_data.head(3)
'''
     서비스 순위                             타이들         가수
0  Melon  1                                 REBEL HEART  IVE (아이브)
1  Melon  2           HOME SWEET HOME(feat. 태양, 대성)   G-DRAGON
2  Melon  3                             나는 반딧불        황가람
'''

# 크롤링 결과를 엑셀파일로 저장
pd_data.to_excel('./files/melon.xlsx', index = False)

#================================================================================

# 버그
driver = webdriver.Chrome()
url = 'https://music.bugs.co.kr/chart'

driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

# 반복문을 이용해 곡과 가수명을 song_data에 저장
song_data = []

rank = 1    # 순위

songs = soup.select('table > tbody > tr')[:100]
len(songs)  # 100개

'''
강사님 코드
songs = soup.select('table.bychart > tbody > tr')
len(songs)

title = song.select('p.title > a')[0].text
singer = song.select('p.artist > a')[0].text
'''

# 제목 뽑기
title = song.select('th > p > a')[0].text
# 가수 뽑기
singer = song.select('td > p > a')[0].text

for song in songs:
    title = song.select('th > p > a')[0].text
    singer = song.select('td > p > a')[0].text
    
    song_data.append(['Bug', rank, title, singer])
    
    rank += 1
    
song_data[0]    #=> ['Melon', 1, 'REBEL HEART', 'IVE (아이브)']

# song_data 리스트를 이용해 데이터프레임 만들기
import pandas as pd

columns = ['서비스','순위','타이들','가수']   # 컬럼 만들기

pd_data = pd.DataFrame(song_data, columns = columns)    # 데이터프레임
pd_data.head(3)
'''
   서비스  순위          타이들         가수
0  Bug   1  REBEL HEART  IVE (아이브)
1  Bug   2     ATTITUDE  IVE (아이브)
2  Bug   3       나는 반딧불        황가람
'''
pd_data.to_excel('./files/bugs.xlsx', index = False)

len(pd_data) # 100개

#==============================================================================
# 지니 1~50
driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200'
# genie.xlsx
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('tr.list > td.info')
len(songs)  # 50개

song = songs[0]

title = song('a')[0].text.replace("\n", "").strip()
#=> 'REBEL HEART'
singer = song('a')[1].text.replace("\n", "").strip()

'''
강사님 코드
songs = soup.select('tbody > tr')
title = song.select('a.title')[0].text.strip()
singer = song.select('a.artist')[0].text.strip()
'''

# 반복문을 이용해 곡과 가수명을 song_data에 저장
song_data = []

rank = 1

for song in songs:
    title = song('a')[0].text.replace("\n", "").strip()
    singer = song('a')[1].text.replace("\n", "").strip()
    
    song_data.append(['Genie', rank, title, singer])
    rank += 1
    
song_data[0] 
import pandas as pd

columns = ['서비스','순위','타이들','가수']   # 컬럼 만들기

pd_data = pd.DataFrame(song_data, columns = columns)    # 데이터프레임
pd_data.head(3)
'''

     서비스  순위                              타이들         가수
0  Genie   1                      REBEL HEART  IVE (아이브)
1  Genie   2                           나는 반딧불        황가람
2  Genie   3  HOME SWEET HOME (Feat. 태양 & 대성)   G-DRAGON
'''

############# 51~100
driver = webdriver.Chrome()
url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20250218&hh=11&rtm=Y&pg=2'
# genie.xlsx
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

songs = soup.select('tr.list > td.info')
len(songs)  # 50개

song = songs[0]

title = song('a')[0].text.replace("\n", "").strip()
#=> '인생찬가'
singer = song('a')[1].text.replace("\n", "").strip()

# 위에 이어서 저장

rank = 51

for song in songs:
    title = song('a')[0].text.replace("\n", "").strip()
    singer = song('a')[1].text.replace("\n", "").strip()
    
    song_data.append(['Genie', rank, title, singer])
    rank += 1
    
song_data[0] 
import pandas as pd

columns = ['서비스','순위','타이들','가수']   # 컬럼 만들기

pd_data = pd.DataFrame(song_data, columns = columns)    # 데이터프레임
pd_data.head(3)
'''
     서비스  순위                            타이들   가수
0  Genie  51                           인생찬가  임영웅
1  Genie  52  Small girl (Feat. 도경수 (D.O.))  이영지
2  Genie  53                           보금자리  임영웅
'''

pd_data.to_excel('./files/genie.xlsx', index = False)









