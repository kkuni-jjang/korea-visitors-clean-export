# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:10:00 2025

@author: KIMMINJI
selenium
"""

from selenium import webdriver

# 크롬브라우저 실행
driver = webdriver.Chrome()

# URL 접속
url = 'https://www.naver.com/' 
driver.get(url)

# 웹페이지 HTML 다운로드
html = driver.page_source           # 모든 문자 가져올 수 있음 / 접속된 페이지 읽어내기 
#------------------------------------------------------------------------------
#### BeautifulSoup.select() ####    *find : 1개 / find_all : 전부
html = '''
<html>
    <head>
    </head>
    <body>
        <h1> 우리동네시장</h1>
            <div class = 'sale'>
                <p id='fruits1' class='fruits'>
                    <span class = 'name'> 바나나 </span>
                    <span class = 'price'> 3000원 </span>
                    <span class = 'inventory'> 500개 </span>
                    <span class = 'store'> 가나다상회 </span>
                    <a href = 'http://bit.ly/forPlaywithData' > 홈페이지 </a>
                </p>
            </div>
            <div class = 'prepare'>
                <p id='fruits2' class='fruits'>
                    <span class ='name'> 파인애플 </span>
                </p>
            </div>
    </body>
</html>
'''
# HTML 문자열 BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 태그명으로 태그 찾기                           * select -> 모든 태그 찾아냄
tags_span = soup.select('span')
'''
[<span class="name"> 바나나 </span>,
 <span class="price"> 3000원 </span>,
 <span class="inventory"> 500개 </span>,
 <span class="store"> 가나다상회 </span>,
 <span class="name"> 파인애플 </span>]

=> 값들이 list로 생성
'''
tags_p = soup.select('p')
'''
[<p class="fruits" id="fruits1">
 <span class="name"> 바나나 </span>
 <span class="price"> 3000원 </span>
 <span class="inventory"> 500개 </span>
 <span class="store"> 가나다상회 </span>
 <a href="http://bit.ly/forPlaywithData"> 홈페이지 </a>
 </p>,
 <p class="fruits" id="fruits2">
 <span class="name"> 파인애플 </span>
 </p>]
'''
# 태그 구조로 위치 찾기 
tags_name = soup.select('span.name')
'''
[<span class="name"> 바나나 </span>, <span class="name"> 파인애플 </span>]
'''

# 상위 구조 활용
tags_banana1 = soup.select('#fruits1 > span.name')
#=> [<span class="name"> 바나나 </span>]

tags_banana2 = soup.select('div.sale > #fruits1 > span.price')
#=> [<span class="price"> 3000원 </span>]
#   div가 sale인 것 중에 p가 fruits1 인 것 중에 span의 class가 price 인 것!

tags_banana3 = soup.select('div.sale span.name')
#=> [<span class="name"> 바나나 </span>]
# > 대신 ' ' 띄어쓰기도 가능 : 내부에서 찾으라는 개념

# 태그 그룹에서 하나의 태그만 선택
tags = soup.select('span.name')
'''
[<span class="name"> 바나나 </span>, <span class="name"> 파인애플 </span>]
'''
tag_1 = tags[0]                          # []인덱스에서 꺼냈기때문에 더이상 인덱스가 아님
#=> <span class="name"> 바나나 </span>

# 태그에서 정보 가져오기 
content = tag_1.text        #=> ' 바나나 '

# 선택한 태그에서 텍스트, 속성 값 가져오기
tags = soup.select('a')
'''
[<a href="http://bit.ly/forPlaywithData"> 홈페이지 </a>]
'''
tag = tags[0]
#=> <a href="http://bit.ly/forPlaywithData"> 홈페이지 </a>
#   인덱스에서 문자열로 꺼내기

content = tag.text
#=> ' 홈페이지 '            *문자열만 출력 가능 ! 

link = tag['href']
#=> 'http://bit.ly/forPlaywithData'


"""
멜론 노래 순위 정보 크롤링
"""
driver = webdriver.Chrome()

url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
'''
한 곡은 <tr>로 열고 닫고 -> 그 안에 <td>는 구성요소 하나하나
'''

# 곡들 꺼내기
songs = soup.select('tr')
len(songs)    #=> 101 개의 tr 존재
songs[0]      # 타이틀명 
'''
<tr>
<th scope="col">
<div class="wrap t_right"><input class="input_check d_checkall" title="곡 목록 전체 선택" type="checkbox"/></div>
</th>
<th scope="col">
<div class="wrap t_center"><span class="rank">순위</span></div>
</th>
<th scope="col">
<div class="wrap none">순위등락</div>
</th>
<th scope="col">
<div class="wrap none">앨범이미지</div>
</th>
<th scope="col">
<div class="wrap none">곡 상세가기</div>
</th>
<th scope="col">
<div class="wrap pd_l_12">곡정보</div>
</th>
<th scope="col">
<div class="wrap pd_l_12">앨범</div>
</th>
<th scope="col">
<div class="wrap pd_l_30">좋아요</div>
</th>
<th scope="col">
<div class="wrap t_center">듣기</div>
</th>
<th scope="col">
<div class="wrap t_center">담기</div>
</th>
<th scope="col">
<div class="wrap t_center">다운</div>
</th>
<th scope="col">
<div class="wrap t_center">뮤비</div>
</th>
</tr>
'''
# 첫 번째 타이틀명 제외하고, 두 번째(인덱스번호 1) 부터 끝까지만 선택
songs = soup.select('tr')[1:]
len(songs)  #=> 100

# 한 개의 곡 정보 지정
song = songs[0]

# 곡 제목 찾기 : <a ~ > </a>
title = song.select('a')
len(title)  # 6개 

title = song.select('span > a')     # span 안에 a태그 찾기
len(title)  # 2개

title = song.select('div.ellipsis.rank01 > span > a')   # 리스트로 자동 출력
'''
[<a href="javascript:melon.play.playSong('1000002721',38444825);" 
 title="REBEL HEART 재생">REBEL HEART</a>]
'''
title = song.select('div.ellipsis.rank01 > span > a')[0]    # 문자열로 출력하기
'''
<a href="javascript:melon.play.playSong('1000002721',38444825);" 
title="REBEL HEART 재생">REBEL HEART</a>
'''
title = song.select('div.ellipsis.rank01 > span > a')[0].text   # text만 출력하기
#=> 'REBEL HEART'

# 가수 찾기 
singer = song.select('div.ellipsis.rank02 > span > a')[0].text
#=> 'IVE (아이브)'



















