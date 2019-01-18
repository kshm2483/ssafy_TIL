import requests
import csv
import json
import os
import re
import urllib.request
from urllib.parse import quote
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bts

movie_codes = []
movie_title = []
audience = []
recourded_at = []

for i in range(10):
    # date
    day_gijun = datetime(2019, 1, 13)
    day_byeon = timedelta(days=-7*i)
    days = day_gijun + day_byeon
    result_days = days.strftime('%Y%m%d')
    # key
    my_key = os.getenv('my_key')
    # url
    url = requests.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={my_key}&targetDt=' + result_days +'&weekGb=0&itemPerPage=10')
    all_data = url.json()
    movie_data = all_data['boxOfficeResult']['weeklyBoxOfficeList']
    # add list
    for i in range(len(movie_data)):
        # 중복 확인 후 리스트 추가
        if movie_data[i]['movieCd'] not in movie_codes:
            movie_codes.append(movie_data[i]['movieCd'])
            movie_title.append(movie_data[i]['movieNm'])
            audience.append(movie_data[i]['audiAcc'])
            recourded_at.append(all_data['boxOfficeResult']['showRange'][-8:])
# CSV 파일 입력
# with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
#     fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
#     writer = csv.DictWriter(f, fieldnames=fieldnames)

#     writer.writeheader()
#     for i in range(len(movie_codes)):
#         writer.writerow({'movie_code': movie_codes[i], 'title': movie_title[i], 'audience':audience[i], 'recorded_at':recourded_at[i]})
# 읽어오기
# with open('boxoffice.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(fieldnames)
#         print(row['movie_code'], row['title'], row['audience'], row['recorded_at'])


# 대표코드, 영화명, 영화명, 개봉연도, 상영시간, 장르, 감독명, 관람등급, 배우1, 배우2, 배우3
movie_nameko = []
movie_nameen = []
movie_nameog = []
prdt_year = []
show_time = []
genres = []
directors = []
watchGrade = []
actors1 = []
actors2 = []
actors3 = []

# movie_codes 들고 반복
for i in range(len(movie_codes)):
    # url
    url = requests.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={my_key}&movieCd={movie_codes[i]}')
    all_data = url.json()
    movie_data = all_data['movieInfoResult']['movieInfo']
    # 리스트에 추가
    movie_nameko.append(movie_data['movieNm'])
    movie_nameen.append(movie_data['movieNmEn'])
    movie_nameog.append(movie_data['movieNmOg'])
    prdt_year.append(movie_data['prdtYear'])
    show_time.append(movie_data['showTm'])
    genres.append(movie_data['genres'][0]['genreNm'])
    directors.append(movie_data['directors'][0]['peopleNm'])
    watchGrade.append(movie_data['audits'][0]['watchGradeNm'])
    # 배우가 없을 경우 공백으로 처리
    if len(movie_data['actors']) >= 3:
        actors1.append(movie_data['actors'][0]['peopleNm'])
        actors2.append(movie_data['actors'][1]['peopleNm'])
        actors3.append(movie_data['actors'][2]['peopleNm'])
    elif len(movie_data['actors']) == 2:
        actors1.append(movie_data['actors'][0]['peopleNm'])
        actors2.append(movie_data['actors'][1]['peopleNm'])
        actors3.append('')
    elif len(movie_data['actors']) == 1:
        actors1.append(movie_data['actors'][0]['peopleNm'])
        actors2.append('')
        actors3.append('')
    else:
        actors1.append('')
        actors2.append('')
        actors3.append('')

with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('Movie_nameKo', 'Movie_nameEN', 'Movie_nameOg','Prdt_year', 'Show_time', 'Genres', 'Directors', 'WatchGrade', 'Actors1', 'Actors2', 'Actors3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(movie_nameko)):
        writer.writerow({'Movie_nameKo': movie_nameko[i], 'Movie_nameEN': movie_nameen[i], 'Movie_nameOg': movie_nameog[i],'Prdt_year': prdt_year[i],
                        'Show_time': show_time[i], 'Genres': genres[i], 'Directors': directors[i], 'WatchGrade': watchGrade[i], 'Actors1': actors1[i], 
                        'Actors2': actors2[i], 'Actors3': actors3[i]})


client_id = os.getenv('naver_id')
client_secret = os.getenv('naver_pw')
for i in range(len(movie_nameko)):
    encText = urllib.parse.quote(f"{movie_nameko[i]}")
    url = "https://openapi.naver.com/v1/search/movie.json?display=1&query=" + encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        print(type(response_body))
    else:
        print("Error Code:" + rescode)