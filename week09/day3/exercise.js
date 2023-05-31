const fib = (n) => {
    let result = [];
    for (let i=0; i<n; i++) {
        i>1?result.push(result[i-1]+result[i-2]):result.push(1)
    }
    return result
}

const fib_sum = (n) => {
    return fib(n).reduce((a,b)=>a+b,0)
}

console.log(fib(5))
console.log(fib_sum(5))