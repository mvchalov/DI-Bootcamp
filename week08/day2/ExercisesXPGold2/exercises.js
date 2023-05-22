// Exercise 1 : Nested Functions
let landscape = function() {

    let result = "";

    let flat = (x) => {
        for(let count = 0; count<x; count++){
            result = result + "_";
        }
    }

    let mountain = (x) => {
        result = result + "/"
        for(let counter = 0; counter<x; counter++){
            result = result + "'"
        }
        result = result + "\\"
    }

    flat(4);
    mountain(4);
    flat(4)

    return result;
}

console.log(landscape())

// Exercise 2 : Closure
const addTo = x => y => x + y;
const addToTen = addTo(10);
console.log(addToTen(3));
// 13

// Exercise 3 : Currying
const curriedSum = (a) => (b) => a + b
console.log(curriedSum(30)(1))
// 31

// Exercise 4 : Currying
const curriedSum2 = (a) => (b) => a + b
const e4add5 = curriedSum2(5)
console.log(e4add5(12))
// 17

// Exercise 5 : Composing
const compose = (f, g) => (a) => f(g(a));
const add1 = (num) => num + 1;
const add5 = (num) => num + 5;
console.log(compose(add1, add5)(10))
// 16