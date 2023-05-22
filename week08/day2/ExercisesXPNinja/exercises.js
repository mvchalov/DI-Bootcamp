// Exercise 1 : Menu
const menu = [
    {
        type : "starter",
        name : "Hummus with Pita"
    },
    {
        type : "starter",
        name : "Vegetable Soup with Houmous peas"
    },
    {
        type : "dessert",
        name : "Chocolate Cake"
    }
]
console.log((menu.find(e=>e.type==="dessert"))?"We have a dessert":"We don't have any desserts today");
console.log(menu.every(e=>e.type==="starter"));
if (!menu.some(e=>e.type==="main course")) {
    menu.push({
        type: "main course",
        name: "Steak"
    })
}
console.log("Main course is added:");
console.log(menu);

const vegetarian = ["vegetable", "houmous", "eggs", "vanilla", "potatoes" ]
menu.forEach(e=>{
    e.vegetarian = (vegetarian.some(i => e.name.indexOf(i) > -1));
})
console.log("Vegetarian flag is added:");
console.log(menu);


// Exercise 2 : Chop Into Chunks
const string_chop = (s,n) => {
    const regex = new RegExp(".{1,"+n+"}", "g");
    return (s.match(regex) ?? []);
}
console.log(string_chop('developers',2));


// Exercise 3 : You Said String ?
const search_word = (s,w) => {
    const counter = [...s.matchAll(w)].length;
    return "'"+w+"' was found "+counter+" time"+((counter!==1)?"s":"")+"."
}
console.log(search_word('The quick brown fox', 'fox'));

// Exercise 4 : Reverse Array
console.log([1,2,3,4,5].reverse());

const reverseArray = a => {
    return (a.length > 1)?[a[a.length-1], reverseArray(a.slice(0, a.length-1))].flat():(a.length===0)?[]:a[0];
}

console.log(reverseArray([1,2,3,4,5]))
console.log(reverseArray([]))
console.log(reverseArray([1,2]))
console.log(reverseArray([1,2,3,4,5,6,7,8,9,10]))


// Exercise 1 : Merge Words

const infiniteCurry = fn => {
    const next = (...args) => {
        return x => (!x)?args.reduce((acc, a) => fn.call(fn, acc, a), ''):next(...args, x);
    };
    return next();
};

const mergeWords = infiniteCurry((x, y) => ([x,y].join` `).trim());

console.log(mergeWords('There')('is')('no')('spoon.')());
console.log(mergeWords('Tell')('me')('a')('story')('I')('never')('heard')('before.')());