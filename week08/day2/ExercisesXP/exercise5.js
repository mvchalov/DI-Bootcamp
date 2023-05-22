// Exercise 5 : Colors #2

const ordinal = ["th","st","nd","rd"];

console.log(colors.map((e,i)=>'"'+(i+1)+((i<3)?ordinal[i+1]:ordinal[0])+" choice is "+e+'."').join(" "));
