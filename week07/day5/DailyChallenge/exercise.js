function verse(counter, take) {
    const currentPhrase = ((counter>1)?counter+" bottles":(counter>0)?"One bottle":"No bottle")+" of beer";
    console.log(currentPhrase, "on the wall");
    console.log(currentPhrase);
    console.log("Take", (take<=counter)?take+"":"every bottle", "down, pass", (take>1)?"them":"it", "around");
    console.log(((counter-take>1)?counter-take+" bottles":(counter-take>0)?"One bottle":"No bottle")+' of beer on the wall\n');
}
let takeCounter = 1;
let counter = 99;
while (counter >= 0) {
    verse(counter, takeCounter);
    counter-=takeCounter;
    takeCounter++;
}