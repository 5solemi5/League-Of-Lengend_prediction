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



| 포지션    |역할|
|--------|---|
| ![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/38b457e8-d0cf-4dd4-90c3-2a85f6dcbc26) 탑(TOP) | 게임 맵의 상단 경로에서 주로 단독으로 플레이하며, 상대 플레이어와의 1대1 대결을 맡는 역할|
| ![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/326fbea0-d1be-42b6-804d-1c79392bb892) 정글(JUNGLE) | 맵 전체를 돌아다니며 각 라인에 관여하고, 중요한 목표물을 확보하는 역할|
| ![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/af7488f0-e72a-4b95-b448-c929e043d651) 미드(MID) | 게임 맵의 중앙 경로에서 주로 단독으로 플레이하며, 상대 플레이어와의 1대1 대결을 맡는 역할|
| ![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/3a2d63a3-b1b0-438b-8f3a-cc5598304b15) 원딜(ADC) | 게임 맵의 하단 경로에서 파트너인 서포터와 함께 플레이하며, 상대 팀과의 2대2 대결을 맡는 역할|
| ![image](https://github.com/5solemi5/League-Of-Lengend_prediction/assets/104000117/6f888067-13c9-444a-8873-4cae991c43bb) 서포터(SUPPORT) | 게임 맵의 하단 경로에서 원딜을 지원하며, 상대 팀과의 2대2 대결에서 원딜을 보호하고 지원하는 역할|


제공된 데이터의 항목은 총 185개로 구성되어 있으며, 전반적으로 다음과 같은 내용으로 정리해볼 수 있다.

| 항목           | 데이터 속성 |
|--------------|--------|
| 플레이어에 대한 데이터 | champlevel, dealt, dealtm, dealtp, dealttaken, deaths, doublekill, dragon, fbassist, fbkill, ftassist, ftkill, goldearned, goldspent, heal, herald, jungle, kills  ...|
| 팀에 대한 데이터    | tdragon, baron, goldearned ... (team 데이터 구성이 플레이어에 대한 데이터와 유사하지만 팀 전체의 정보를 담고 있음 )|
| 라인전 전후에 대한 데이터 | turretkills, visionscore, visionwardsbuy ...|

여기서 중요하게 고려되는 대략적인 항목들은 다음과 같다. 

| 데이터 속성 | 데이터의 의미 | 중요한 이유 |
|-------------|--------------|-------------|
| kda | Kill/Death/Assist의 비율 | 게임 내에서 플레이어의 성과를 가장 잘 나타내는 지표 중 하나이며, 높은 KDA는 승률과 긍정적인 상관관계가 있다. |
| dpd | 챔피언에게 넣은 데미지 / 데스 수(데스가 0일경우 챔피언에게 넣은 데미지) | 데미지 효율성을 나타내는 지표로, 높은 dpd는 플레이어가 데미지를 효율적으로 가하고 있음을 나타내며, 승률과 긍정적인 상관관계가 있다. |
| dpm | 챔피언에게 넣은 데미지 / 게임시간 | 게임 시간당 데미지를 나타내는 지표로, 높은 dpm은 플레이어가 끊임없이 활동하며 데미지를 가하고 있음을 나타내며, 승률과 긍정적인 상관관계가 있다. |
| dpg | 챔피언에게 넣은 데미지 / 총 사용골드(사용골드가 0일경우 챔피언에게 넣은 데미지) | 골드 대비 데미지 효율성을 나타내는 지표로, 높은 dpg는 골드를 효율적으로 사용하고 있음을 나타내며, 승률과 긍정적인 상관관계가 있다. |
| dtpm | 챔피언에게 받은 데미지 / 게임시간 | 게임 시간당 받은 데미지를 나타내는 지표로, 낮은 dtpm은 플레이어가 데미지를 효과적으로 피하고 있음을 나타내며, 승률과 긍정적인 상관관계가 있다. |
| goldearned (플레이어) | 플레이어가 획득한 골드 양 | 골드는 아이템을 구매하는 데 사용되며, 플레이어의 성능 향상에 중요한 역할을 한다. |
| goldearned (팀) | 팀 전체가 획득한 골드 양 | 팀 전체의 골드 양은 팀의 전체적인 성능과 승률에 영향을 미친다. |
| turretkills | 타워 파괴 횟수 | 타워를 파괴하는 것은 맵 컨트롤과 골드 획득에 중요하며, 승리로 이어질 가능성이 높다. |
| visionscore | 시야 점수 | 시야 점수는 맵의 정보를 얼마나 잘 파악하고 있는지를 나타내며, 이는 승률에 큰 영향을 미친다. |
| dragon (플레이어) | 플레이어가 처치한 용의 수 | 용을 처치하면 팀 전체에게 버프를 제공하므로, 용을 많이 처치한 팀이 승리할 가능성이 높다. |
| dragon (팀) | 팀이 처치한 용의 수 | 팀 전체가 처치한 용의 수는 팀의 전략적 승리를 나타내며, 승률에 큰 영향을 미친다. |
| baron | 바론 처치 여부 | 바론을 처치하면 굉장히 강력한 버프를 얻게 되어, 승리에 큰 도움이 된다. |
| kills (플레이어) | 플레이어가 처치한 적의 수 | 적을 많이 처치하면 골드와 경험치를 획득하며, 이는 승률 향상에 도움이 된다. |
| deaths (플레이어) | 플레이어의 사망 횟수 | 사망하면 일정 시간동안 게임에 참여할 수 없어 팀에 부정적인 영향을 미치므로, 사망 횟수가 적을수록 승률이 높아진다. |


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

| id | team | feature | TOP | MID | JUG | SPT | ADC |
|---|---|---|---|---|---|---|---|
| 6667524844 | 100 | kda | 1.85714 | 3.0 | 4.6 | 2.75 | 1.5 |
| 6667524844 | 100 | dpd | 3932.0 | 5131.0 | 3796.8 | 2350.88 | 2417.3 |
| 6667524844 | 100 | dpm | 786.775 | 733.349 | 542.658 | 537.599 | 690.986 |
| 6667524844 | 100 | dpg | 1.85672 | 1.85987 | 1.4232 | 1.69662 | 1.66837 |
| 6667524844 | 100 | dtpm | 1191.57 | 688.471 | 1455.58 | 792.692 | 725.317 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 6669000775 | 200 | dpm | 607.414 | 429.801 | 117.99 | 433.068 | 456.0 |
| 6669000775 | 200 | dpg | 1.64422 | 1.52872 | 0.392641 | 1.30673 | 1.4873 |
| 6669000775 | 200 | dtpm | 508.272 | 500.921 | 687.895 | 403.853 | 386.702 |
| 6669000775 | 200 | win | 1 | 1 | 1 | 1 | 1 |
| 6669000775 | 200 | tier | G | G | G | P | G |

[0825_game_data.pkl의 대략적 형태]

| id | team | feature | TOP | MID | JUG | SPT | ADC |
|---|---|---|---|---|---|---|---|
| 6667524895 | 100 | kda | 1.4 | 1.5 | 2.5 | 10.0 | 9.5 |
| 6667524895 | 100 | dpd | 1862.4 | 1802.67 | 3430.25 | 4052.5 | 12114.5 |
| 6667524895 | 100 | dpm | 360.465 | 418.684 | 531.135 | 313.742 | 937.897 |
| 6667524895 | 100 | dpg | 1.13561 | 1.51379 | 1.44736 | 1.19279 | 1.61204 |
| 6667524895 | 100 | dtpm | 751.664 | 605.574 | 1081.16 | 510.735 | 565.548 |
| ... | ... | ... | ... | ... | ... | ... | ... |
| 6669000761 | 200 | dpm | 743.729 | 651.093 | 482.922 | 628.931 | 345.713 |
| 6669000761 | 200 | dpg | 2.30143 | 1.60665 | 1.36441 | 2.28239 | 1.06544 |
| 6669000761 | 200 | dtpm | 1005.61 | 745.19 | 1175.67 | 589.632 | 628.539 |
| 6669000761 | 200 | win | 0 | 0 | 0 | 0 | 0 |
| 6669000761 | 200 | tier | E | P | E | P | P |

[0825_game_data_is_platinum.pkl의 대략적 형태]



[0825_game_data_is_platinum_norm.pkl의 대략적 형태]


# 3. 승패예측 모델

## 3.1 모델 개요
CNN을 썼다. 단순한 합산을 썼다.

## 3.2 성능

주어진 결과를 보면 모델의 성능이 고려되는 플래티넘 이상 (4.5만건), 데이터 전체 (20만건)에서 모두 높은 정확도를 보여주고 있다.

| 날짜   | 전체 데이터 예측 일치 횟수 | 전체 경기 수 | 전체 데이터 정확도 | 플래티넘 이상 데이터 예측 일치 횟수 | 플래티넘 이상 경기 수 | 플래티넘 이상 데이터 정확도 |
|--------|-----------------------|--------------|--------------------|---------------------------------|----------------------|------------------------|
| 0825   | 194566                | 201545       | 약 0.97 | 43700                           | 44962                | 약 0.97     |
| 0915   | 168771                | 178580       | 약 0.95 | 27141                           | 28209                | 약 0.96     |
| 0917   | 248497                | 264395       | 약 0.94 | 23912                           | 25208                | 약 0.95     |


# Reference
https://www.pharmnews.com/news/articleView.html?idxno=213910

https://www.gamemeca.com/view.php?gid=1652452

https://www.youtube.com/watch?v=C3GouGa0noM

https://www.leagueoflegends.com/ko-kr/news/

https://developer.riotgames.com/


## 3.3 소결
* 성능에 대한 의미
* 핵심 데이터 항목에 대한 추정 및 분석

# 4. 결론 및 배운점
