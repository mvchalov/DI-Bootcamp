// Exercise 4 : Colors

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

console.log(colors.map((e,i)=>'"'+(i+1)+"# choice is "+e+'."').join(" "));
console.log((colors.indexOf("Violet") > -1)?"Yeah":"No...");