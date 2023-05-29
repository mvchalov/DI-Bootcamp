const holder = document.querySelector(".container");
const form = document.createElement("form");
form.method = "POST"
form.action = "index2.html"
form.innerHTML = `
        <input type="text" placeholder="Your name" name="name">
        <textarea placeholder="Enter your comment" name="message"></textarea>
        <button type="submit">Send</button>
    `;
holder.appendChild(form);