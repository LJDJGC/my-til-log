class Player {
  constructor(name) {
    this.name = name;
  }

  introduce() {
    console.log(`私は ${this.name} です。`);
  }

  static checkWinner(playerA,playerB) {
    console.log(`${playerA.name} と ${playerB.name} の勝敗を判定します...`);
  }
}


const p1 = new Player("Alice");
const p2 = new Player("Bob");

p1.introduce();

p1.checkWinner(p1, p2);