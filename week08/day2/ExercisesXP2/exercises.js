// Exercise 1 : Find The Sum

const findSum = (a,b) => {
    return a+b
}


// Exercise 2 : Kg And Grams
function kgGramDeclared(weight) {
    return weight*1000
}

const kgGramExpressed = function (weight) {
    return weight*1000
}

// declared: named function, expressed: anonymous function available through the variable/const name

const kgGramArrow = (weight) => {
    return weight*1000
}
console.log(kgGramArrow(55));
console.log(kgGramDeclared(55));
console.log(kgGramExpressed(55));


// Exercise 3 : Fortune Teller

const createItem = (content) => {
    const item = document.createElement("p");
    item.appendChild(document.createTextNode(content));
    document.querySelector(".col").appendChild(item)
}

(function fortuneTeller(...vars) {
    createItem(`You will be a ${vars[3]} in ${vars[2]}, and married to ${vars[1]} with ${vars[0]} kids.`)
})(4, 'Bob', 'London', 'manager');


// Exercise 4 : Welcome
const users = {
    "John" : "john.jpg",
    "Mary" : "mary.jpg"
};
((user) => {
    const userInfo = document.createElement("div");
    userInfo.innerHTML = `<a href="#"><img src="${users[user]}" alt="${user}"><span>${user}</span></a>`
    document.querySelector(".navbar .container-fluid").appendChild(userInfo);
})("John")


// Exercise 5 : Juice Bar


const makeJuice = (size) => {

    const ingredients = [];
    const addIngredients = (...items) => {
        for (const item of items) {
            ingredients.push(item)
        }
    }
    addIngredients("kiwi", "melon", "apple");
    addIngredients("banana", "cherry", "strawberry");
    createItem(`The client wants a ${size} juice, containing ${ingredients.join(", ")}.`)
}

makeJuice("small");