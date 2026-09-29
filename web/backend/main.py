from typing import Union
import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import uvicorn

origins = [
    "*"
]

app = FastAPI()

#cors 에러 방지코드
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # cookie 포함 여부를 설정한다. 기본은 False
    allow_methods=["*"],    # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다.
    allow_headers=["*"],	# 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.
)

#riot api에 요청을보낼때 붙이는 헤더입니다. 발급받은 api-key는 환경변수 RIOT_API_KEY로 설정해주세요
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": os.environ["RIOT_API_KEY"]
    }

#기본적인 summoner정보를 가져오는 코드
@app.get("/getSummonerInfo/{summoonerName}")
def get_summoner_info(summoonerName: str):
    result = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summoonerName, headers=header)
    if(result.status_code == 200):
        js_result = result.json()
        summonerInfo = {'name': js_result['name']
                        ,'profileIconId': js_result['profileIconId']
                        ,'id': js_result['id']
                        , 'puuid': js_result['puuid']
                        , 'summonerLevel': js_result['summonerLevel']}
        return summonerInfo

#해당 summoner의 리그정보중에서 솔로랭크(RANKED_SOLO_5x5) 티어만 리턴하는 코드 "랭크가 없을경우에는 {}리턴"
@app.get("/getSummonerLeagueById/{summonerId}")
def get_summoner_League(summonerId: str):
    result = requests.get("https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerId, headers=header)
    if (result.status_code == 200):
        js_result = result.json()
        for league in js_result:
            if(league['queueType'] == 'RANKED_SOLO_5x5'):
                return league
            else:
                return {}

#요청갯수만큼 솔로랭크(queue=420)의 게임 MatchId를 리스트로 리턴하는 코드
@app.get("/getMatchList/{summonerPuuid}/{count}")
def get_summoner_Matchs(summonerPuuid: str, count: int):
    result = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + summonerPuuid
                          + '/ids?queue=420&start=0&count=' + str(count), headers=header)
    if (result.status_code == 200):
        js_result = result.json()
        return js_result

#해당 MatchId게임의 매치정보를 리턴하는 코드
@app.get("/getMatchInfo/{matchId}")
def get_match_info(matchId: str):
    result = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/" + matchId, headers=header)
    if (result.status_code == 200):
        js_result = result.json()
        return js_result

#모델을 사용하여 승리예측결과를 리턴하는코드
@app.get("/matchPredict/")
def get_match_info(xpm: float, gpm: float, dpm: float, dpd: float):
    print(xpm,gpm,dpm,dpd)
    # 모델 로드
    loaded_model = tf.keras.models.load_model('./my_model.h5')
    # 입력 데이터 준비
    input_data = [[xpm,gpm,dpm,dpd]]  # 예시 입력 데이터

    # 예측 생성
    predictions = loaded_model.predict(input_data)
    prediction_values = predictions.tolist()
    print(prediction_values[0])
    return {'win': prediction_values[0][0]}