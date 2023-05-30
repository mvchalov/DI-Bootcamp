const holder = document.querySelector(".container");
const form = document.createElement("form");
form.innerHTML = `
        <input type="text" placeholder="First name" name="name">
        <input type="text" placeholder="Last name" name="surname">
        <button type="submit">Send</button>
    `;
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = JSON.stringify(Object.fromEntries(new FormData(form)));
    const outputDiv = document.createElement("div");
    outputDiv.innerHTML = data;
    holder.appendChild(outputDiv)
})
holder.appendChild(form);
