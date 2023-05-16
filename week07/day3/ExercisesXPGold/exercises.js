// Exercise 1 : Divisible By Three
let numbers = [123, 8409, 100053, 333333333, 7];
numbers.forEach(e=>{
    console.log(e, "is", ((e%3!=0)?"not ":"")+"divisible by three")
})

// Exercise 2 : Attendance
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
}
let username = prompt("Enter your name");
if (Object.keys(guestList).includes(username.toLowerCase())) {
    console.log(`Hi, I'm ${username} and I'm from ${guestList[username.toLowerCase()]}`)
}
else {
    console.log("Hi, I'm a guest.")
}

// Exercise 3 : Playing With Numbers
let age = [20,5,12,43,98,55];
let old = 0;
let sum = 0;
for (let i=0; i<age.length; i++) {
    sum += age[i];
    if (old < age[i]) {
        old = age[i]
    }
}
console.log("Sum:", sum);
console.log("Highest age in group:", old);