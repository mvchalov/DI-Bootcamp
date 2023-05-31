const holder = document.querySelector(".container");
const output = (content) => {
    const item = document.createElement("img");
    item.src = content.images.original.url;
    item.alt = content.id;
    holder.appendChild(item);
}

(async () => {
    try {
        const response = await fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My");
        let data = await response.json();
        for (const item of data.data) {
            output(item)
        }
    }
    catch (e) {
        console.error(e, "has occurred")
    }

})();