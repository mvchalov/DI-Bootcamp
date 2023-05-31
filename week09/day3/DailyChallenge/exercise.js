const holder = document.querySelector(".container");

const output = (content) => {
    const innerHolder = document.createElement("div");
    const item = document.createElement("img");
    item.src = content.images.original.url;
    item.alt = content.id;
    innerHolder.appendChild(item);
    const button = document.createElement("button");
    button.innerHTML = "Delete";
    innerHolder.appendChild(button);
    button.addEventListener("click", e => {
        e.preventDefault();
        e.target.parentElement.remove()
    })
    holder.appendChild(innerHolder);
}

const initDeleteAll = () => {
    if (!holder.querySelector("form a")) {
        const deleteAllButton = document.createElement("a");
        deleteAllButton.innerHTML = "Delete all";
        deleteAllButton.href = "#";
        deleteAllButton.addEventListener("click", (e) => {
            e.preventDefault();
            holder.querySelectorAll("div").forEach(item => {
                item.remove()
            })

        })
        holder.querySelector("form").appendChild(deleteAllButton);
    }
}

const getData = async (data) => {
    try {
        const responce = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${data.gifQuery}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`);
        let item = await responce.json();
        output(item.data);
        initDeleteAll()
    }
    catch (e) {
        console.error(e, "has occurred")
    }
}

(() => {
    const headline = document.createElement("h1");
    headline.textContent = "Find a gif";
    holder.appendChild(headline);
    const form = document.createElement("form");
    form.innerHTML = `
        <input type="text" name="gifQuery">
        <button type="submit">Find</button>
    `;
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        getData(Object.fromEntries(new FormData(e.target)));
    })
    holder.appendChild(form);
})()