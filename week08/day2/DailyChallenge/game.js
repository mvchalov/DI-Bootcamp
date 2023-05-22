const gameInfo = [
    {
        username: "john",
        team: "red",
        score: 5,
        items: ["ball", "book", "pen"]
    },
    {
        username: "becky",
        team: "blue",
        score: 10,
        items: ["tape", "backpack", "pen"]
    },
    {
        username: "susy",
        team: "red",
        score: 55,
        items: ["ball", "eraser", "pen"]
    },
    {
        username: "tyson",
        team: "green",
        score: 1,
        items: ["book", "pen"]
    },
];

const createItem = (content) => {
    const item = document.createElement("p");
    item.appendChild(document.createTextNode(content));
    document.body.appendChild(item)
}

const usernames = [];

gameInfo.forEach(e=>{
    usernames.push(e.username+'!')
})

const winners = [];

gameInfo.forEach(e=>{
    (e.score > 5)?winners.push(e.username):false;
})

createItem(`Usernames: ${usernames.join(", ")}`);
createItem(`Winners: ${winners.join(", ")}`);
createItem(`Score: ${gameInfo.reduce((a,e)=>a + e.score,0)}`)



