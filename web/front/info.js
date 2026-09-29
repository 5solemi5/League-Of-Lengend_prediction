const matchDataList = [];
let id, puuid, name, profileiconId;

async function moveSearchPage(params) {
    const input = document.getElementById("summonerName");

    //프로필 정보 가져오는 api call
    let getprofile = await getApi("/getSummonerInfo/"+ input.value)
    id = getprofile.id;
    puuid = getprofile.puuid;
    name = getprofile.name;
    profileiconId = getprofile.profileIconId;

    //프로필아이콘 영역에 해당 프로필아이콘 url을 이미지소스로 삽입
    const prifileIcon = document.getElementById("profileIcon");
    prifileIcon.src = `https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/profile-icons/${profileiconId}.jpg`

    //레벨 영역에 소환사 레벨을 innerText로 추가
    const level = document.getElementById("summonerLevel");
    level.innerText = getprofile.summonerLevel;

    //소환사 이름 영역에 innerText에 name을 추가
    const profileName = document.getElementById("summonerProfileName");
    profileName.innerText = name;

    //리그 정보 가져오는 api call
    let getleagueInfo = await getApi("/getSummonerLeagueById/"+ id);
    const summonerTier = document.getElementById("summonerTier");
    if(getleagueInfo){
        //리그정보가 있을 경우에는 티어+랭크+포인트 문자열 추가
        summonerTier.innerText = getleagueInfo.tier + getleagueInfo.rank + ' ' + getleagueInfo.leaguePoints + 'LP'
    }
    else {
        //리그정보가 있을 경우에는 UNRANKED문자열 추가
        summonerTier.innerText = "UNRANKED"
    }

    //길이 5만큼의 매치리스트 요청
    let getMatchList = await getApi("/getMatchList/"+ puuid + '/' + 5);
    const matchList = document.getElementById("matchList");
    // matchList의 모든 자식 요소를 삭제합니다.
    while (matchList.firstChild) {
        matchList.removeChild(matchList.firstChild);
    }

    //매치리스트의 매치들의 정보를 api 콜
    await Promise.all(getMatchList.map(async(matchId)=>{
        let getMatchList = await getApi("/getMatchInfo/"+ matchId);
        if(getMatchList) matchDataList.push(getMatchList);
    }))
    //게임을 생성시간순으로 정렬
    matchDataList.sort((a,b)=>b.info.gameCreation - a.info.gameCreation);
    //게임데이터 기반으로 매치리스트 html생성
    matchDataList.map(async(matchData)=>{
        const match = document.createElement("div");
        let mydata = matchData?.info.participants?.find((p)=>p.summonerId == id)
        match.style.marginLeft = '4px'
        match.style.marginRight = '4px'
        match.style.width = '150px'
        match.style.height = '50px'
        match.style.display = "flex"
        match.style.position = "relative"
        match.style.alignItems = "center"
        match.onclick = ()=>{printSelectedMatch(matchData)}
        if(mydata){
            if(mydata.win)
                match.style.backgroundColor = '#D6E6FF'
            else
                match.style.backgroundColor = '#FFD6D6'
        }

        const cImg = document.createElement("img");
        cImg.style.width = '50px'
        cImg.style.height = '50px'
        cImg.src = "http://ddragon.leagueoflegends.com/cdn/13.17.1/img/champion/" + mydata.championName + '.png'
        match.appendChild(cImg)

        const KDALabel = document.createElement("div");
        KDALabel.style.marginLeft = "8px";
        KDALabel.innerText = mydata.kills + '/' + mydata.deaths + '/' + mydata.assists;
        match.appendChild(KDALabel)

        matchList.appendChild(match)
    })

}

async function printSelectedMatch(matchData){
    let mydata = matchData?.info.participants?.find((p)=>p.summonerId == id)
    //매치데이터를 활용하여 승리예측결과를 화면에 출력해주세요
    const winPredict = document.getElementById("winPredict");
    let gpm,xpm,dpm,dpd;
    gpm = mydata.goldEarned / (matchData?.info.gameDuration || 1)
    xpm = mydata.champExperience / (matchData?.info.gameDuration || 1)
    dpm = mydata.totalDamageDealtToChampions / (matchData?.info.gameDuration || 1)
    dpd = mydata.totalDamageDealtToChampions / (mydata.deaths || 1)

    let getPredict = await getApi(`/matchPredict/?gpm=${xpm}&xpm=${gpm}&dpm=${dpm}&dpd=${dpd}` );
    console.log(getPredict?.win)

    const prediction = document.createElement("div");
    prediction.style.width = '80px'
    prediction.style.height = '30px'
    prediction.style.right = "0px"
    prediction.style.backgroundColor = "white"
    prediction.innerText = "예측" + (getPredict?.win > 0.5 ? "승리" : "패배");
    winPredict.appendChild(prediction)

    //매치데이터를 활용하여 룬 정보를 화면에 출력해주세요
    const rune = document.getElementById("rune");

    //매치데이터를 활용하여 스킬빌드를 화면에 출력해주세요
    const skill = document.getElementById("skill");

    //매치데이터를 활용하여 아이템빌드를 화면에 출력해주세요
    const item = document.getElementById("item");

}

async function getApi(url, params){
    let returnValue;
    //http프로토콜을 위하여 fetch함수 사용
    await fetch('http://127.0.0.1:8000' + url)
    .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not ok');
        }
        return response.json(); // JSON 응답을 파싱하여 JavaScript 객체로 변환
    })
    .then(data => {
        // JSON 데이터를 JavaScript 객체로 처리
        returnValue = data
      })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });

    return returnValue;
}