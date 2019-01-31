from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import os
import csv
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

# 5월 20일부터 d-day 카운트 출력
@app.route('/dday')
def dday():
   date = datetime.datetime(2019, 5, 20)
   today = datetime.datetime.now()
   td = date - today
   return '{} 일 남았습니다.'.format(td.days)
   
# variable routing
@app.route('/hi/<string:name>')
def greeting(name=None):
    # return '안녕, {}'.format(name)
    # greeting.html 로 위처럼 안녕 누구누구를 출력해주세요.
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:num>')
def cube(num):
    return f'{num**3}'

# for문 작동
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)

@app.route('/google')
def google():
    return render_template('google.html')
    
# 핑퐁    / GET방식
@app.route('/ping')
def ping():
    return render_template('ping.html')
@app.route('/pong')
def pong():
    # name = request.args['name'] 도 똑같이 동작하나 error로 페이지 날림
    name = request.args.get('name')
    msg = request.args.get('msg')
    return render_template('pong.html', name=name, msg=msg)
    
# new핑퐁 / POST방식
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')
@app.route('/pong_new', methods=['POST'])
def pong_new():
    name = request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)
    
# OPGG
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)

# CSV
@app.route('/timeline')
def timeline():
    # 지금까지 기록되어있는 방명록을 보여주자.
    with open('timeline.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        timelines = []
        for row in reader:
            timelines.append(row)

    return render_template('timeline.html', timelines=timelines)
    
@app.route('/timeline/create')
def timeline_create():
    name = request.args.get('username')
    msg = request.args.get('message')
    
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer = csv.DictWriter(f, fieldnames=['username', 'message'])
        writer.writerow({'username': name, 'message': msg})
        
    return redirect('/timeline')
    # return render_template('timeline_create.html', username=name, message=msg)

if  __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)