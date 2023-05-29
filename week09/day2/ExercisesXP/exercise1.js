const compareToTen = (number) => {
    return new Promise((resolve, reject) => {
        (number < 10)?resolve(number+" is correct"):reject("Error! "+number+" is incorrect");
    })
}

//In the example, the promise should reject
compareToTen(15)
    .then(result => console.log(result))
    .catch(error => console.log(error))

//In the example, the promise should resolve
compareToTen(8)
    .then(result => console.log(result))
    .catch(error => console.log(error))