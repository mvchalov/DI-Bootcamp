const makeAllCaps = (inData) => {
    return new Promise((resolve, reject) => {
        if (inData.reduce((x,y) => x?typeof y != 'string'?false:x:x, true)) {
            resolve(inData.map(e=>e.toUpperCase()))
        }
        else {
            reject("Not all the values are strings")
        }
    })
}

const sortWords = (inData) => {
    return new Promise((resolve, reject) => {
        if (inData.length > 4) {
            resolve(inData.sort())
        }
        else {
            reject("The array is too short")
        }
    })
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

//in this example, you should see in the console,
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
    .catch(error => console.log(error))