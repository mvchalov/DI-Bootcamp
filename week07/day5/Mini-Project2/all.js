const operandValue = ["+", "-", "X", "/", "="];
let prevNumber = -1;
let operand = -1;

function calculateResult(x,y,operandValueIdx) {
    switch (operandValueIdx) {
        case 0: document.querySelector("input").value = +x + +y;
                break;
        case 1: document.querySelector("input").value = +x - +y;
            break;
        case 2: document.querySelector("input").value = +x * +y;
            break;
        case 3: document.querySelector("input").value = +x / +y;
            break;
    }
}

function resetCalculator() {
    document.querySelectorAll("a").forEach(item=>{
        if (item.classList.contains("active")) {
            item.classList.remove("active")
        }

    })
    operand = -1;
    prevNumber = -1;
}

function runCalculation(currOperand) {
    if ((currOperand == 4)&&(operand > -1)) {
        if (prevNumber > -1) {
            calculateResult(prevNumber, document.querySelector("input").value, operand);
        }
        else {
            calculateResult(document.querySelector("input").value, document.querySelector("input").value, operand);
        }
        resetCalculator();
    }
    else {
        if (operand > -1) {
            if (prevNumber > -1) {
                calculateResult(prevNumber, document.querySelector("input").value, currOperand);
            }
            else {
                calculateResult(document.querySelector("input").value, document.querySelector("input").value, currOperand);
            }
            resetCalculator();
        }
        else {
            operand = currOperand;
            prevNumber = document.querySelector("input").value;
            document.querySelector("input").value = 0;
        }
    }
}

function initCalculator() {
    const inputNumber = document.createElement("input");
    inputNumber.value = 0;
    const buttonsHolder = document.createElement("div");
    for (let i=0; i<10; i++) {
        const buttonNumber = document.createElement("a");
        buttonNumber.classList.add("buttonNumber");
        buttonNumber.innerHTML = i+"";
        buttonsHolder.appendChild(buttonNumber);
    }
    const buttonNumber = document.createElement("a");
    buttonNumber.classList.add("buttonNumber");
    buttonNumber.innerHTML = ".";
    buttonsHolder.appendChild(buttonNumber);
    for (let i=0; i<5; i++) {
        const buttonOperand = document.createElement("a");
        buttonOperand.classList.add("buttonOperand");
        buttonOperand.innerHTML = operandValue[i];
        buttonsHolder.appendChild(buttonOperand);
    }
    const buttonReset = document.createElement("button");
    buttonReset.innerHTML = "reset";
    buttonReset.classList.add("buttonReset");
    buttonsHolder.appendChild(buttonReset);
    const buttonClear = document.createElement("button");
    buttonClear.innerHTML = "clear";
    buttonClear.classList.add("buttonClear");
    buttonsHolder.appendChild(buttonClear);
    const holder = document.querySelector(".calculator");
    holder.appendChild(inputNumber);
    holder.appendChild(buttonsHolder);
}

function initListeners() {
    const numberButtons = document.querySelectorAll(".buttonNumber");
    numberButtons.forEach(item=>{
        item.addEventListener("click", (e)=>{
            let currValue = document.querySelector("input").value;
            if (e.target.innerHTML==".") {
                if (currValue == "") {
                    currValue = "0."
                }
                else {
                    currValue += ".";
                }
            }
            else {
                if (currValue == "0") {
                    currValue = +e.target.innerHTML;
                }
                else {
                    currValue += +e.target.innerHTML;
                }
            }
            document.querySelector("input").value = currValue
        })
    });

    document.querySelector(".buttonClear").addEventListener("click", ()=>{
        document.querySelector("input").value = "0";
    });

    document.querySelector(".buttonReset").addEventListener("click", ()=>{
        document.querySelector("input").value = "0";
        prevNumber = 0;
        operand = -1;
    })

    document.querySelectorAll(".buttonOperand").forEach(item=>{
        item.addEventListener("click", (e)=>{
            e.target.classList.add("active");
            runCalculation(operandValue.indexOf(e.target.innerHTML))
        })
    })
}

initCalculator();
initListeners();