const delayedPromise = () => {
    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            try {
                resolve("Here's the success string")
            }
            catch {
                reject("Ooops something went wrong")
            }
        }, 4000);

    })
}

delayedPromise()
    .then(result => console.log(result))
    .catch(result => console.log("Error:", result));


const delayedPromise2 = () => {
    setTimeout(() => {
        Promise.resolve("Success").then(result => console.log(result))
    }, 4000)
}

delayedPromise2()