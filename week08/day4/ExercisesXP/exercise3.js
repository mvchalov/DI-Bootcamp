const users = { user1: 18273, user2: 92833, user3: 90315 };

console.log(Object.entries(users));
console.log(Object.entries(users).map(e=>{
    e[1] *= 2;
    return e
}));