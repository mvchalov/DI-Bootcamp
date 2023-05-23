// Exercise 1 : Analyzing The Map Method
// [1, 2, 3].map(num => {
//     if (typeof num === 'number') return num * 2;
//     return ;
// });
// [2, 4, 6]


// Exercise 2: Analyzing The Reduce Method
// [[0, 1], [2, 3]].reduce(
//     (acc, cur) => {
//         return acc.concat(cur);
//     },
//     [1, 2],
// );
// [1, 2, 0, 1, 2, 3]


// Exercise 3 : Analyze This Code
// const arrayNum = [1, 2, 4, 5, 8, 9];
// const newArray = arrayNum.map((num, i) => {
//     console.log(num, i);
//     alert(num);
//     return num * 2;
// })
// What is the value of i ?
// index (in this case, 0...5)


// Exercise 4 : Nested Arrays
const array = [[1],[2],[3],[[[4]]],[[[5]]]].flat(2);
console.log(array);

const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]].map(e=>e.join(" "));
console.log(greeting);

console.log(greeting.join(" "))

const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]]
console.log(trapped.flat(100))