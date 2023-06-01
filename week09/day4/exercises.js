const findDup = (a) => {
    const res = {}
    for (const i of a) {
        Object.keys(res).includes(i)?res[i]++:res[i]=1
    }
    return Object.keys(res)
}

console.log(findDup(['A', 'B', 'A', 'C', 'B']))
console.log(findDup(['A', 'B', 'C', 'K', 'D']))
console.log(findDup([]))
console.log(findDup(['A', 'A', 'A']))

const revStr = (s) => {
    return s.split``.reverse().join``
}

console.log(revStr('hello world'))


const sortArr = (a) => {
    let flag = true;
    while (flag) {
        flag = false;
        for (let i=1; i<a.length; i++) {
            if (a[i]<a[i-1]) {
                flag = true;
                let tmp = a[i];
                a[i] = a[i-1];
                a[i-1] = tmp
            }
        }
    }
    return a;
}

console.log(sortArr([1,2,3,0,7,4]))