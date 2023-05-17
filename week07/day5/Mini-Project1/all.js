let computerNumber = Math.round(Math.random()*10);

function playTheGame() {
    const container = document.querySelector(".container");
    if (container.classList.contains("hidden")) {
        container.classList.remove("hidden");
    }
    else {
        alert("Type the number between 0 and 10 in the input!")
    }
}

function guessTheNumber(userNumber) {
    if (userNumber == computerNumber) {
        computerNumber = Math.round(Math.random()*10);
        alert("You're the winner!")
        document.querySelector(".container").classList.add("hidden")
    }
    else {
        if (userNumber < computerNumber) {
            alert("Your number is smaller then the computer’s, guess again")
        }
        else {
            alert("Your number is bigger then the computer’s, guess again")
        }
    }
}


document.querySelector("button").addEventListener("click", ()=>{
    playTheGame()
})

document.querySelector("a").addEventListener("click",()=>{
    const enteredValue = document.querySelector("input").value;
    if (!enteredValue||(!((+enteredValue <= 10)&&(+enteredValue >= 0)))) {
        alert("Please, enter a number between 0 and 10!");
    }
    else {
        guessTheNumber(enteredValue)
    }
    document.querySelector("input").value = "";
})

