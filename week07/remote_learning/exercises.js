// Exercise 1

var num = 8;
var num = 10;
console.log(num);
// 10


// Exercise 2

function numbers() {
    for (let i = 0; i < 5; i += 1) {
        console.log(i);
    }
}
numbers();


// Exercise 3

var money = 0;

function updateBalance() {
    let income = 1000;
    let expenses = 500;
    return income - includeVAT(expenses);
}

function includeVAT(expenses) {
    const VAT = .1;
    return expenses * (1+VAT);
}

money += updateBalance();
console.log(money)