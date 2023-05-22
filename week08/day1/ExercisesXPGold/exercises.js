// Exercise 1 : Select A Kind Of Music
const genres = document.querySelector("#genres");
const classic = document.createElement("option");
classic.value = "classic";
classic.innerHTML = "Classic";
classic.defaultSelected = true;
genres.appendChild(classic);


// Exercise 2: Delete Colors
const removecolor = () => {
    (Array.from(document.querySelectorAll("#colorSelect option")).filter(e=>e.selected)[0]).remove()
}

document.querySelector("input[type='button']").addEventListener("click", removecolor);


// Exercise 3 : Create A Shopping List
let shoppingList=[];
let holder = document.querySelector("#root");
const form = document.createElement("form");
form.innerHTML = "<input type='text' name='item'><button type='submit'>Add Item</button><button type='reset'>Clear all</button>"
holder.appendChild(form);
holder.appendChild(document.createElement("div"));


const updateList = () => {
    const listHolder = document.querySelector("#root div");
    listHolder.innerHTML = shoppingList.join("<br>");
    console.log(shoppingList)
}

document.querySelector("#root button[type='submit']").addEventListener("click", e=>{
    e.preventDefault();
    if (e.target.previousSibling.value.match(/[a-zA-Z0-9 .-]/g)) {
        shoppingList.push(e.target.previousSibling.value);
    }
    e.target.previousSibling.value = "";
    updateList();
});

document.querySelector("#root button[type='reset']").addEventListener("click", e=>{
    shoppingList = [];
    updateList();
})