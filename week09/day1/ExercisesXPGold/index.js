const holder = document.querySelector(".container");
const form = document.createElement("form");
form.method = "GET";
form.action = "output.html";
form.innerHTML = `
    <div><label for="name">First name</label><input type="text" name="name" id="name"></div>
    <div><label for="lastname">Last name</label><input type="text" name="lastname" id="lastname"></div>
    <button type="submit">Submit</button>
`;
holder.appendChild(form);