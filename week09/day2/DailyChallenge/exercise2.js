const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`

let inData = "";

document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    inData = e.target.querySelector("input").value;
    toJs(morse)
        .then(data => toMorse(data)
            .then(translated => joinWords(translated))
        )
})

const toJs = (morseJson) => {
    return new Promise((resolve, reject) => {
        try {
            resolve(JSON.parse(morseJson))
        }
        catch (error) {
            reject(error)
        }
    })
}

const toMorse = (morseJS) => {
    return new Promise((resolve, reject) => {
        inData.toLowerCase().split``.filter(e=>!e.match(new RegExp("["+Object.keys(morseJS).join``+" "+"]"))).length > 0?reject("Input data error"):resolve(inData.split` `.map(e=> e.split``.map(x=>morseJS[x]).join(" <span>|</span> ")))
    })
}

const joinWords = (morseTranslation) => {
    if (document.querySelector(".container div")) {
        document.querySelector(".container div").remove()
    }
    const outputHolder = document.createElement("div");
    outputHolder.innerHTML = morseTranslation.join("<br>");
    document.querySelector(".container").appendChild(outputHolder)
}


