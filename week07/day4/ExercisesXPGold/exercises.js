// Exercise 1 : Is_Blank
function isBlank(s) {
    return (s.length == 0)
}

console.log(isBlank(''));
console.log(isBlank('abc'));


// Exercise 2 : Abbrev_name
function abbrevName(s) {
    let items = s.split(" ");
    items[items.length-1] = items[items.length-1][0]+'.'
    return items.join(" ")
}

console.log(abbrevName("Robin Singh"));
console.log(abbrevName("Anna Maria Dines"));


// Exercise 3 : SwapCase
function swapCase(s) {
    return s.split``.map(e=>(e.match(/[a-z]/g))?e.toUpperCase():(e.match(/[A-Z]/g))?e.toLowerCase():e).join``
}

console.log(swapCase("The Quick Brown Fox"))


// Exercise 4 : Omnipresent Value
function isOmnipresent(a, x) {
    return a.reduce((q,p)=>(!p.includes(x))?false:q, true)
}

console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6));


// Exercise 5 : Red Table
// In index.html