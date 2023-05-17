// Exercise 1: Random Number

const randomNumber = Math.random()*100+1;
const evenNumbers = [];
for (let i=0; i<=randomNumber; i++) {
    if (i%2 === 0) {
        evenNumbers.push(i)
    }
}
console.log(evenNumbers)


// Exercise 2: Capitalized Letters
function capitalize(s) {
    return [s.toLowerCase().split``.map((e,i)=>(i%2===0)?e.toUpperCase():e).join``, s.toLowerCase().split``.map((e,i)=>(i%2!=0)?e.toUpperCase():e).join``]
}

console.log(capitalize("abcdef"))


// Exercise 3 : Is Palindrome?
function isPalindrome(s) {
    return (s.toLowerCase().split``.reverse().join`` === s.toLowerCase())
}
console.log(isPalindrome("madam"));
console.log(isPalindrome("madame"));


// Exercise 4 : Biggest Number
function biggestNumberInArray(a) {
    return a.reduce((x,y)=>(+y > x)?+y:x, 0)
}
console.log(biggestNumberInArray([-1,0,3,100, 99, 2, 99]));
console.log(biggestNumberInArray(['a', 3, 4, 2]));
console.log(biggestNumberInArray([]));

// Exercise 5: Unique Elements
function createSet(a) {
    return new Set(a)
}

console.log(createSet([1,2,3,3,3,3,4,5]));
console.log(createSet([1,6,6,3,1,3,6,5]));


// Exercise 6 : Calendar
// index.html