// Exercise 3 : Is It A String ?

const isString = (s) => {
    return (typeof s == 'string')?true:false
}

console.log(isString('hello'));
console.log(isString([1, 2, 4, 0]));