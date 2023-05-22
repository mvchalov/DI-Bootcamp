// Exercise 6 : Bank Details

let bankAmount = 0;
const VAT = .17;
const details = ["+200", "-100", "+146", "+167", "-2900"];
bankAmount = details.reduce((a,e)=>+e+a,bankAmount);
console.log(bankAmount)