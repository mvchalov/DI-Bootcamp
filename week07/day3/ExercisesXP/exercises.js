// Part I - Review About Arrays
const people = ["Greg", "Mary", "Devon", "James"];
console.log(people);
people.shift()
console.log(people);
people[2] = "Jason";
console.log(people);
people.push("Max");
console.log(people);
console.log(people.indexOf("Mary"))
const other_people = people.slice(1,people.length-1)
console.log(other_people);
console.log(people.indexOf("Foo"));
const last = people[people.length-1];
console.log(last);

// Part II - Loops
const colors = ["white", "red", "blue", "black", "green"]
for (let i=0; i<colors.length; i++) {
    console.log("My #"+(i+1), "choice is", colors[i])
}
const suffixes = ["st", "nd", "rd", "th"];
for (let i=0; i<colors.length; i++) {
    console.log("My", (i+1)+((i<4)?suffixes[i]:suffixes[suffixes.length-1]), "choice is", colors[i])
}

// Exercise 3 : Repeat The Question
let n = 0;
do {
    n = prompt("Enter a number > 10: ");
} while ((!Number.isInteger(+n))||(+n<10))

// Exercise 4 : Building Management
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log("The number of floors in the building:", building["numberOfFloors"]);
console.log("How many apartments are on the floors 1 and 3:", building["numberOfAptByFloor"]["firstFloor"], "and", building["numberOfAptByFloor"]["thirdFloor"]);
console.log("The name of the second tenant:", building["nameOfTenants"][1], "("+building["numberOfRoomsAndRent"][building["nameOfTenants"][1].toLowerCase()][0], "rooms)");
let sum = 0;
for (let i=0; i< Object.values(building["numberOfRoomsAndRent"]).length; i++) {
    if (i!==1) {
        sum += Object.values(building["numberOfRoomsAndRent"])[i][1];
    }
}
if (sum > building["numberOfRoomsAndRent"][building["nameOfTenants"][1].toLowerCase()][1]) {
    building["numberOfRoomsAndRent"][building["nameOfTenants"][1].toLowerCase()][1] += 200;
}
console.log("Current Dan's rent is", building["numberOfRoomsAndRent"][building["nameOfTenants"][1].toLowerCase()][1])

// Exercise 5 : Family
const family = {
    "father": "John",
    "mother": "Mary",
    "son": "Gary"
}
for (const [key, value] of Object.entries(family)) {
    console.log(key+":", value)
}

// Exercise 6 : Rudolf
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}
console.log((Object.entries(details)).flat().join` `);

// + with for as said in the instructions
let str = "";
for (const [key, value] of Object.entries(details)) {
    str+=key+' '+value+' ';
}
console.log(str);

// Exercise 7 : Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
console.log(names.sort().reduce((a,b)=>a+b[0], ""));