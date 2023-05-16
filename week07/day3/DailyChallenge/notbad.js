// Daily Challenge: Not Bad
function checkSentence(sentence) {
    const wordNot = sentence.indexOf("not");
    const wordBad = sentence.indexOf("bad");
    if ((wordBad > wordNot)&&(wordBad > 0)&&(wordNot > 0)) {
        sentence = sentence.substring(0, wordNot) + "good" + sentence.substring(wordBad+3, sentence.length)
    }
    return sentence
}

console.log(checkSentence("This dinner is not that bad ! You cook well"));
console.log(checkSentence("This movie is not so bad !"));
console.log(checkSentence("This dinner is bad !"));
console.log(checkSentence("Not this dinner is bad !"));