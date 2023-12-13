<div align=center>

![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/77ba308a-dfc7-4b6a-ab32-9b4f879cd722)


# 🗡️💻 League Of Lengend 승패예측 딥러닝🏹🎮 
  
Riot Games에서 제공하는 게임 데이터를 활용한 게임 승패 예측 딥러닝 프로젝트
 
<h2>:heavy_check_mark:Tech Stack</h2>
<img src="https://img.shields.io/badge/PyTorch-E34F26?style=flat-square&logo=PyTorch&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>

</div>

# 1. 개 요
League Of Lengend(이하 LOL)는 현재 전 세계적으로 1억 명 이상의 월별 활동 사용자를 보유하며,[<sup>[1]</sup>](https://www.pharmnews.com/news/articleView.html?idxno=213910) 가장 인기 있는 온라인 게임 중 하나로 인정받고 있다. 전 세계 여러 국가와 지역에서 운영되는 전문 e스포츠 리그를 통해 수백만 명의 관중을 끌어들이며, 2022년 항저우 아시안 게임에서는 정식 종목으로 채택될 만큼 그 영향력은 이미 검증되었다.[<sup>[2]</sup>](https://www.gamemeca.com/view.php?gid=1652452) 또한, 게임의 캐릭터들과 스토리는 단순히 게임을 넘어서 여러 형태의 미디어, 예를 들어 애니메이션 시리즈, 만화, 음악 등에 활용되며, 강력한 문화적 영향력을 발휘하고 있다. 이런 지표들은 리그 오브 레전드가 전 세계적으로 널리 인정받고 사랑받는 게임임을 보여준다.

![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/d56aefae-eab1-4462-aebe-60121041e297)

<div align=center>
  
[[자료: 'GODS' MV 캡쳐본]](https://www.youtube.com/watch?v=C3GouGa0noM)

</div>

LOL을 개발한 Riot Games는 비단 게임 자체의 재미뿐만 아니라 분석할 수 있는 데이터를 무료로 공개하고 있다. Riot Games API에서는 LOL 소환사의 개인적인 게임 정보와 더불어 경기 데이터까지 제공한다. 통계적으로 하루 24시간 동안 수집되는 경기 수는 약 20만 건에 달하며, 소정의 절차를 거치면 손쉽게 얻을 수 있다.[<sup>[3]</sup>](https://www.leagueoflegends.com/ko-kr/news/)

![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/fcb3669b-cd06-41d6-bec5-7d58c3d90f09)

<div align=center>
  
[[자료: Riot Games 홈페이지 일부]](https://developer.riotgames.com/)

</div>


"LOL에서 다양한 변수를 고려하여 게임의 승패를 어떻게 가장 정확하게 예측할 수 있을까?" 이 문제를 해결하기 위해, 우리는 데이터 전처리, 탐색적 데이터 분석, 피처 엔지니어링, 모델 선택 및 튜닝 등의 단계를 거칠 예정이다. 이 과정에서, 우리는 각 변수가 승패에 어떠한 영향을 미치는지 이해하고, 그것을 바탕으로 승패를 가장 잘 예측하는 모델을 구축하려고 한다.

이번 프로젝트에서는 20만 건의 하루치 LOL 게임 데이터를 분석하여 승패를 예측하는 모델을 만들 것이다.

# 2. 데이터
## 2.1 데이터 소스
이번 프로젝트에 활용할 데이터는 온라인 게임 코칭 전문기업인 더매치랩(The Match LAB)에서 가공한 LOL 게임 데이터를 바탕으로 한다. 데이터는 2023년 8월 25일, 9월 15일, 9월 17일 각각 하루 동안 수집된 LOL 경기에 대한 세부 항목들로 구성되어 있다.
https://developer.riotgames.com/

## 2.2 탐색적 데이터 분석
데이터는 5대5 솔로 랭크 경기 약 20만 건으로 구성되어 있으며, 포지션별로 데이터가 구분되어 있다. 5가지 포지션에 대한 내용은 다음과 같다.

* LOL 게임에 대한 간략한 설명
* 영상을 삽입하던지

| 포지션    |역할|
|--------|---|
| 탑(TOP) |???|
| 정글(JUNGLE) | ???|

제공된 데이터의 항목은 총 185개로 구성되어 있으며, 전반적으로 다음과 같은 내용으로 정리해볼 수 있다.

| 항목           | 데이터 속성 |
|--------------|--------|
| 플레이어에 대한 데이터 | ???    |
| 팀에 대한 데이터    | ???    |
|라인전 전후에대한 데이터 |???|

여기서 중요하게 고려되는 항목들은 다음과 같다. (10개 이상)

| 데이터 속성 | 데이터의 의미     | 중요한 이유 |
|-------|-------------|--------|
| KDA   | Kill/Death/Assist의 비율 |
| 팀에 대한 데이터 | ???         |
| 라인전 전후에대한 데이터 | ???         |

## 2.3 데이터 전처리
20만 건의 경기 데이터는 수준 별로 편차가 어느정도 존재할 것으로 예상된다. 따라서 일정 수준 이상의 데이터로 지표의 상관성을 통해 승패예측 모델을 만드는 것이 합리적일 것이다.

이에 이번 프로젝트에서는 다음과 같이 정의되는 LOL게임의 등급체계(tier)를 바탕으로, 모든 플레이어가 플래티넘 이상인 경기를 추출하여 분석해보고자 한다.

* 티어에 대한 정보 (표)
* 티어별 히스토그램
* 플래티넘 이상인 경기의 수

도출된 플래티넘 이상의 경기에 대해서, 핵심 데이터 속성으로 ???, ???, ??? 등을 추출했다. 그 이유는 ~~~때문이다. 그리고 승패를 예측하는 것이기 때문에, 경기 데이터를 기준으로 데이터 속성별 정규화(normalize)를 수행했다. 

## 2.4 데이터 프레임 설계

탐색적 데이터 분석과 데이터 전처리를 통해 다음과 같은 데이터 프레임을 만들고자 한다.

| Id  | 팀  | 주요지표 | TOP |MID|
|-----|-----|---------|-----|---|
| 고유번호 | Red/Blue | kda, dpd, ...| ... |...|

# 3. 승패예측 모델

## 3.1 모델 개요
CNN을 썼다. 단순한 합산을 썼다.

## 3.2 성능
플래티넘 이상 4.5만건
데이터 전체 20만건

# Reference
[<sup>[1]</sup>](https://www.pharmnews.com/news/articleView.html?idxno=213910)
[<sup>[2]</sup>](https://www.gamemeca.com/view.php?gid=1652452)
[<sup>[3]</sup>](https://www.leagueoflegends.com/ko-kr/news/)
https://developer.riotgames.com/


## 3.3 소결
* 성능에 대한 의미
* 핵심 데이터 항목에 대한 추정 및 분석

# 4. 결론 및 배운점
