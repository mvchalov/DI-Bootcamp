const KEYS = [
    {
        key: 'A',
        description: 'Boom'
    },
    {
        key: 'S',
        description: 'Clap'
    },
    {
        key: 'D',
        description: 'HiHat'
    },
    {
        key: 'F',
        description: 'Kick'
    },
    {
        key: 'G',
        description: 'OpenHat'
    },
    {
        key: 'H',
        description: 'Ride'
    },
    {
        key: 'J',
        description: 'Snare'
    },
    {
        key: 'K',
        description: 'Tink'
    },
    {
        key: 'L',
        description: 'Tom'
    }
]

function initKeyboard() {
    KEYS.forEach(item=>{
        const itemContainer = document.createElement("div");
        itemContainer.innerHTML = `<h2>${item.key}</h2><p>${item.description}</p>`;
        item["soundObj"] = new Audio("./sounds/"+item["description"].toLowerCase()+".wav");
        itemContainer.appendChild(item["soundObj"]);
        itemContainer.querySelector("audio").load();
        itemContainer.addEventListener("click", e=>{
            const currAudio = e.currentTarget.querySelector("audio");
            if (currAudio&&(currAudio.readyState > 0)) {
                currAudio.currentTime = 0;
                currAudio.play();
            }
        })
        document.querySelector(".container").appendChild(itemContainer)
    })
}

initKeyboard()