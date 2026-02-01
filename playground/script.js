let hamster = {
  stomach: [],

  eat(food) {
    // this.stomach.push の代わりに this.stomach に代入する
    this.stomach = [food];
  }
};

let speedy = {
   __proto__: hamster
};

let lazy = {
  __proto__: hamster
};

// Speedy は食べ物を見つけました
speedy.eat("apple");
alert( speedy.stomach ); // apple

// Lazy の胃は空っぽです
alert( lazy.stomach ); // <nothing>