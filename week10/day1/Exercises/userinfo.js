const {getUsers} = require("./users");

getUsers().then((data) => {
    console.log(data)
})
