# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:17:11 2025

@author: KIMMINJI
youtube 데이터(10개 페이지) 및 시각화
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# webdriver로 크롬 브라우저 실행
browser = webdriver.Chrome()
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'
browser.get(url)

# 페이지 정보 가져오기
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

# BeautifulSoup으로 tr 태그 추출
channel_list = soup.select('tr')
len(channel_list)   # 102
channel_list[0]
'''
<tr>
<th class="rank"><a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=rank&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">순위 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="td_img">이미지</th>
<th class="subject">제목</th>
<th class="subscriber_cnt"><a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=subscriber_cnt&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">구독자순 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="view_cnt"><a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=view_cnt&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">View순 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="video_cnt"><a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=video_cnt&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">Video순 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="hit"><a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=wr_hit&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">조회수 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
</tr>
'''
channel_list = soup.select('form > table > tbody > tr')
len(channel_list)   # 100


# 카테고리 추출 : <p class = category>
channel = channel_list[0]
category = channel.select('p.category')[0].text.strip()


# 채널명 : <h1><a ~~> 채널명 </a></h1>
title = channel.select('h1 > a')[0].text.strip()
#=> 'BLACKPINK'

# 구독자 수(subscriber_cnt) 
# View 수(view_cnt)
# 동영상 수 추출(video_cnt)
'''
<td class="subscriber_cnt">
<td class="view_cnt">
<td class="video_cnt">
'''
subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text
#------------------------------------------------------------------------------
## 페이지별 URL : 10개
page = 1
# format 사용
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={}'.format(page) 
                                                                         #{}로 블럭처리
#=> 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1'
'''
# f 예약어 사용
url = f'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}'
'''
#------------------------------------------------------------------------------
results = [] # <= [title, category, subscriber, view, video]

for page in range(1,11):
       url = f'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}' 
       browser.get(url)
       time.sleep(2)        # sleep : 초 단위 / 잠시 재우는 함수
       html = browser.page_source
       soup = BeautifulSoup(html, 'html.parser')
       
       channel_list = soup.select('form > table > tbody > tr')
       
       for channel in channel_list :
           title = channel.select('h1 > a')[0].text.strip()
           category = channel.select('p.category')[0].text.strip()
           subscriber = channel.select('.subscriber_cnt')[0].text
           view = channel.select('.view_cnt')[0].text
           video = channel.select('.video_cnt')[0].text
           
           data = [title, category, subscriber, view, video]
           results.append(data)

# 데이터 컬럼명을 설정하고 엑셀 파일로 저장
df = pd.DataFrame(results)
df.columns = ['title', 'category', 'subscriber', 'view', 'video']
df.to_excel('./files/youtube_rank.xlsx', index = False)
            





























