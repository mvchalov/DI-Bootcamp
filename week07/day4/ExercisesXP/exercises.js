// Exercise 1 : Find The Numbers Divisible By 23
function isDivisible() {
    let result = [];
    for (let i=0; i<500; i++) {
        if (i % 23 === 0) {
            result.push(i);
        }
    }
    return result;
}

function runFunction(func, param) {
    const result = func(param)

    console.log("Outcome :", result.join` `);
    console.log("Sum :", result.reduce((a,b)=>a+b, 0))
}

runFunction(isDivisible)

// Bonus: Add a parameter divisor to the function.

function isDivisibleByDivisor(divisor) {
    let result = [];
    for (let i=0; i<500; i++) {
        if (i % divisor === 0) {
            result.push(i);
        }
    }
    return result;
}

runFunction(isDivisibleByDivisor, 23)
runFunction(isDivisibleByDivisor, 3)
runFunction(isDivisibleByDivisor, 45)


// Exercise 2 : Shopping List
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

const shoppingList =  ["banana", "orange", "apple", "kiwi"];

function myBill() {
    let result = 0;
    for (const item of shoppingList) {
       result += prices[item]??0;
       if (Object.keys(stock).includes(item)) {
           stock[item] = Math.max(stock[item]-1, 0);
       }
    }
    return result
}

console.log(myBill());
console.log(stock);

// Exercise 3 : What’s In My Wallet ?
function changeEnough(itemPrice, amountOfChange) {
    const value = [0.25, 0.1, 0.05, 0.01];
    return (amountOfChange.reduce((a,b,i)=>a+b*value[i],0) >= itemPrice)
}

console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));

// // Exercise 4 : Vacations Costs
function hotelCost(nights) {
    const pricePerNight = 140;
    return pricePerNight*nights
}

function planeRideCost(destination) {
    const prices = {
        "London": 183,
        "Paris": 220,
        "default": 300
    }
    return prices[destination]??prices["default"]
}

function rentalCarCost(days) {
    const rentPerDay = 40;
    return days*rentPerDay
}

function getInputData(params) {
    const result = [];
    for (const item in params) {
        while (true) {
            let value = prompt(item);
            if ((typeof value == params[item])||((params[item]=="number")&&(!isNaN(parseFloat(value))))) {
                result.push(value);
                break;
            }
        }
    }
    return result
}

function totalVacationCost() {
    const inputData = getInputData({
        "days of stay" : "number",
        "destination" : "string",
        "days of car rent" : "number"
    })
    return hotelCost(inputData[0])+planeRideCost(inputData[1])+rentalCarCost(inputData[2])
}

console.log(totalVacationCost())

// Exercise 5 : Users
console.log(document.querySelector("div"));
const lis = document.querySelectorAll("li");
for (const item of lis) {
    if (item.innerHTML == "Pete") {
        item.innerHTML = "Richard"
    }
    else {
        if (item.innerHTML == "Sarah") {
            item.remove()
        }
    }
}

const firstLis = document.querySelectorAll("ul li:first-of-type");console.log(firstLis)

for (const item of firstLis) {
    item.innerHTML = "Max"
}

document.querySelectorAll("ul").forEach(e => {
    e.classList.add("student_list")
})

document.querySelector("ul").classList.add("university", "attendance");

document.querySelector("div").style.padding = "10px 20px";
document.querySelector("div").style.backgroundColor = "lightblue";

for (const item of lis) {
    if (item.innerHTML.indexOf("Max") > -1) {
        item.style.display = "none";
    }
    else {
        if (item.innerHTML.indexOf("Richard") > -1) {
            item.style.border = "2px solid darkblue"
        }
    }
}

document.body.style.fontSize = "2em";

document.querySelectorAll("div").forEach(e=>{
    if (e.style.backgroundColor == "lightblue") {
        console.log(e.childNodes);
        alert("Hello"+Array.from(e.querySelector("ul").childNodes).map(e=>e.innerHTML).join(" "))
    }
})

// Exercise 6 : Change The Navbar
// ex6.html
