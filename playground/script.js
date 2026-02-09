  function outer(){
    const outerVar = 'Hey I am the outer Var';

    function inner(){
      const innerVar = "hey I am an inner var";
      console.log(innerVar);
      console.log(outerVar);
    }
  }
