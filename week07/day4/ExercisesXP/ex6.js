//  Exercise 6 : Change The Navbar

document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation");

const newLi = document.createElement("li");
const newA = document.createElement("a");
newA.innerHTML = "Logout";
newA.setAttribute("href", "http://google.com")
newLi.appendChild(newA);
document.querySelector("ul").appendChild(newLi);

const newP = document.createElement("p");
newP.textContent = document.querySelector("ul").firstElementChild.textContent + " " + document.querySelector("ul").lastElementChild.textContent
document.body.appendChild(newP);