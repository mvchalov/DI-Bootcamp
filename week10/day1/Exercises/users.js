const getUsers = async () => {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users");
        return await response.json()
    }
    catch (e) {
        console.error(e, "is happened")
    }
}

module.exports = {
    getUsers
}