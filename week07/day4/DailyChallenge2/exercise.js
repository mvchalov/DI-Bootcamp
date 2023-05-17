function getInData() {
    return prompt("Please, enter the phrase:")
}

function outputPhrase(phrase) {
    const maxLength = phrase.split` `.reduce((x,y)=>(y.length > x)?y.length:x, 0);
    console.log('*'.repeat(maxLength+4))
    for (const item of phrase.split` `) {
        console.log('* ' + item + ' '.repeat(maxLength-item.length) + ' *')
    }
    console.log('*'.repeat(maxLength+4))
}

outputPhrase(getInData())