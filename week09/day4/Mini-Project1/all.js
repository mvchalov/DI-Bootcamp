class Person {

    initButton() {
        const button = document.createElement("button");
        button.innerHTML = "Find a person";
        button.addEventListener("click", () => {
            try {
                this.fetchPerson()
            }
            catch (error) {
                console.error("During the data fetching", error, "has occurred.")
            }
        });
        this.holder.appendChild(button);
    }

    initInnerHolder() {
        this.innerHolder = document.createElement("div");
        this.innerHolder.classList.add(this.innerHolderClass);
        this.holder.appendChild(this.innerHolder);
    }

    initRender() {
        this.initInnerHolder();
        this.initButton()
    }

    async fetchPerson() {
        const urlAPI = "https://www.swapi.tech/api/people/";
        const personId = Math.trunc(Math.random()*84);
        this.render();
        try {
            const response = await fetch(urlAPI+personId);
            const data = await response.json();
            this.render(data.result.properties);
        }
        catch (e) {
            console.error("During the data retrieving", e, "has occurred.")
        }
    }

    render(data=undefined) {
        if (!data) {
            this.innerHolder.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" width="124" height="124" preserveAspectRatio="xMidYMid" style="margin:auto;display:block;shape-rendering:auto" viewBox="0 0 100 100"><path fill="none" stroke="#f5c037" stroke-dasharray="42.76482137044271 42.76482137044271" stroke-linecap="round" stroke-width="8" d="M24.3 30C11.4 30 5 43.3 5 50s6.4 20 19.3 20c19.3 0 32.1-40 51.4-40C88.6 30 95 43.3 95 50s-6.4 20-19.3 20c-19.3 0-32.1-40-51.4-40z" style="transform:scale(1);transform-origin:50px 50px"><animate attributeName="stroke-dashoffset" dur="1s" keyTimes="0;1" repeatCount="indefinite" values="0;256.58892822265625"/></path></svg>                 
            `
        }
        else {
            this.innerHolder.innerHTML = `
                <h2>${data.name}</h2>
                <ul>
                    <li><span>Height:</span>${data.height}</li>
                    <li><span>Gender:</span>${data.gender}</li>
                    <li><span>Birth year:</span>${data.birth_year}</li>
                    <li><span>Home world:</span>${data.homeworld}</li>
                </ul>
            `
        }
    }

    constructor() {
        this.holder = document.querySelector(".container");
        this.innerHolderClass = "innerContainer";
        this.innerHolder = undefined;
        this.initRender()
    }
}

(() => {
    let canvas = document.getElementById('canvas'),
        ctx = canvas.getContext('2d'),
        w = canvas.width = window.innerWidth,
        h = canvas.height = window.innerHeight,

        hue = 55,
        stars = [],
        count = 0,
        maxStars = 1400,

        canvas2 = document.createElement('canvas'),
        ctx2 = canvas2.getContext('2d');


    canvas2.width = 100;
    canvas2.height = 100

    let half = canvas2.width/2,
        gradient2 = ctx2.createRadialGradient(half, half, 0, half, half, half);

    gradient2.addColorStop(0.025, '#fce5a2');
    gradient2.addColorStop(0.1, 'hsl(' + hue + ', 61%, 33%)');
    gradient2.addColorStop(0.25, 'hsl(' + hue + ', 64%, 6%)');
    gradient2.addColorStop(1, 'transparent');

    ctx2.fillStyle = gradient2;
    ctx2.beginPath();
    ctx2.arc(half, half, half, 0, Math.PI * 2);
    ctx2.fill();

    function random(min, max) {
        if (arguments.length < 2) {
            max = min;
            min = 0;
        }

        if (min > max) {
            var hold = max;
            max = min;
            min = hold;
        }

        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    function maxOrbit(x,y) {
        var max = Math.max(x,y),
            diameter = Math.round(Math.sqrt(max*max + max*max));
        return diameter/2;
    }

    let Star = function() {

        this.orbitRadius = random(maxOrbit(w,h));
        this.radius = random(60, this.orbitRadius) / 12;
        this.orbitX = w / 2;
        this.orbitY = h / 2;
        this.timePassed = random(0, maxStars);
        this.speed = random(this.orbitRadius) / 50000;
        this.alpha = random(2, 10) / 10;

        count++;
        stars[count] = this;
    }

    Star.prototype.draw = function() {
        var x = Math.sin(this.timePassed) * this.orbitRadius + this.orbitX,
            y = Math.cos(this.timePassed) * this.orbitRadius + this.orbitY,
            twinkle = random(10);

        if (twinkle === 1 && this.alpha > 0) {
            this.alpha -= 0.05;
        } else if (twinkle === 2 && this.alpha < 1) {
            this.alpha += 0.05;
        }

        ctx.globalAlpha = this.alpha;
        ctx.drawImage(canvas2, x - this.radius / 2, y - this.radius / 2, this.radius, this.radius);
        this.timePassed += this.speed;
    }

    for (var i = 0; i < maxStars; i++) {
        new Star();
    }

    function animation() {
        ctx.globalCompositeOperation = 'source-over';
        ctx.globalAlpha = 0.8;
        ctx.fillStyle = 'hsla(' + hue + ', 5%, 6%, 1)';
        ctx.fillRect(0, 0, w, h)

        ctx.globalCompositeOperation = 'lighter';
        for (var i = 1, l = stars.length; i < l; i++) {
            stars[i].draw();
        }

        window.requestAnimationFrame(animation);
    }

    animation();

})();

new Person();



