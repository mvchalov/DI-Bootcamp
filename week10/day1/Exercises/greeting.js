const greeting = (name) => {
    console.log("Hello", name)
}

const goodbye = (name) => {
    console.log(`Goodbye ${name}`)
}

module.exports = {
    greeting,
    goodbye
}