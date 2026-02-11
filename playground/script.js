function  createGame(gameName){
  let score = 0;

  return function win(){
    score ++;
    return `Your name ${gameName} score is ${score}`
  }
}

const hockeyGame = createGame('Hockey');
const sccerGame = createGame('Soccer');