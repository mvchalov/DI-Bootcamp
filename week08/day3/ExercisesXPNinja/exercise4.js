const letters = ['x', 'y', 'z', 'z'];

const lettersNew = {}
for (const letter of letters) {
    lettersNew[letter] = lettersNew[letter]?lettersNew[letter]+1:1;
}
console.log(lettersNew)
console.log(letters.reduce((a,e)=>{
    a[e]?a[e]++:a[e]=1;
    return a;
},{}))