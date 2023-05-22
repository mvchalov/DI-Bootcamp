const testArray = [1,2,3,4,5,2,3,4,5,1];
const testArray2 = [NaN, 0, 15, false, -22, '',undefined, 47, null];

// Exercise 1: Sum Elements
console.log(testArray.reduce((a,e)=>a+e,0));

// Exercise 2 : Remove Duplicates
console.log(Array.from(new Set(testArray)));

// Exercise 3 : Remove Certain Values
console.log(testArray2.filter(e=>((typeof e == 'number')&&(e!==0)&&(!isNaN(e)))));

// Exercise 4 : Repeat Please !
console.log('Ha!'.repeat(3));

const repeat = (s,n) => {
    return s.padEnd(s.length*n, s);
}
console.log(repeat('Ha!',3));

// Exercise 5 : Turtle & Rabbit
const startLine = '     ||<- Start line';
let turtle = '🐢';
let rabbit = '🐇';
turtle = " ".repeat(startLine.indexOf("|")) + turtle;
rabbit = rabbit.padStart(rabbit.length+startLine.indexOf("|"), " ");
console.log(startLine);
console.log(turtle);
console.log(rabbit);

// What happens when you run turtle = turtle.trim().padEnd(9, '='); ?
// It pads turtle with '=' till reaching the length of 9