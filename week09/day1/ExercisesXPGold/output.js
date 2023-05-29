const holder = document.querySelector(".container");
const header = document.createElement("h1");
header.innerHTML = "The submitted data:";
holder.appendChild(header);
const data = window.location.search.substr(1).split("&")
const inner = data.map(e=>`<li><b>${e.split("=")[0]}</b> ${e.split("=")[1]}</li>`)
const list = document.createElement("ul");
list.innerHTML = inner.join``;
holder.appendChild(list);