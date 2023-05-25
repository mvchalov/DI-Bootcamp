class coloringGame {

    addElement({node, value, event, listener, container}) {
        const newElement = document.createElement(node);
        newElement.innerHTML = value;
        if (event !== "") {
            newElement.addEventListener(event, listener);
        }
        document.querySelector(container).appendChild(newElement)
        return newElement;
    }

    initControls() {
        const elements = [
            {
                node: "div",
                value: "",
                event: "",
                listener: undefined,
                container: this.container
            },
            {
                node: "div",
                value: "",
                event: "",
                listener: undefined,
                container: this.container
            },
            {
                node: "button",
                value: "Clear",
                event: "click",
                listener: ()=>this.initGrid(),
                container: this.container + this.containerInner
            },
            {
                node: "div",
                value: "",
                event: "",
                listener: undefined,
                container: this.container + this.containerInner
            }
        ]
        for (const item of elements) {
            this.addElement(item)
        }
    }

    initColors() {
        for (const item in this.colors) {
            const currentColor = this.addElement({
                node: "div",
                value: "",
                event: "click",
                listener: (event) => {
                    this.currentColor = this.colors[event.target.getAttribute("data-color")];
                    document.querySelectorAll(this.container + this.containerColors + this.containerInner).forEach(e=> e.classList.remove("active"))
                    event.target.classList.add("active");
                },
                container: this.container + this.containerColors
            })
            currentColor.setAttribute("data-color", item);
            currentColor.style.backgroundColor = this.colors[item];
        }
    }

    initGrid() {
        const containerGrid = document.querySelector(this.container + this.containerGrid);
        containerGrid.innerHTML = (new Array(3000).fill('<div></div>')).join``;
        containerGrid.childNodes.forEach(e=>e.addEventListener("click", event => event.target.style.backgroundColor = this.currentColor))
    }

    initBoard() {
        this.initControls();
        this.initColors();
        this.initGrid()
    }

    constructor() {
        this.colors = {
            "white": "#fff",
            "gray": "#999",
            "darkgray": "#555",
            "black": "#000",
            "yellow": "#ff0",
            "orange": "#f90",
            "orangered": "#f40",
            "red": "#f00",
            "darkred": "#600",
            "lightgreen": "#9f9",
            "green": "#0f0",
            "yellowgreen": "#470",
            "darkgreen": "#130",
            "lightblue": "#0df",
            "skyblue": "#59f",
            "blue": "#00f",
            "darkblue": "#117",
            "peach": "#fca",
            "pink": "#f9f",
            "plum": "#808",
            "violet": "#407"
        };
        this.currentColor = this.colors.white;
        this.container = ".containerGame";
        this.containerColors = "> div:first-of-type > div";
        this.containerGrid = " > div:last-of-type";
        this.containerInner = "> div";
        this.initBoard()
    }
}

const coloringGameInstance = new coloringGame();