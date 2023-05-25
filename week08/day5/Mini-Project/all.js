class roboGame {

    updateView(inData) {
        const cards = this.container.children;
        Array.from(cards).forEach(e=>{
            e.innerHTML.toLowerCase().includes(inData.toLowerCase())?e.classList.remove(this.hiddenClass):e.classList.add(this.hiddenClass)
        })
    }

    initHeader() {
        const header = document.createElement("header");
        header.innerHTML = `
            <h2>RoboFriends</h2>
            <input type="text">
        `;
        header.lastElementChild.addEventListener("keydown", e=>{
            setTimeout(() => {
                this.updateView(e.target.value)
            }, 100);
        })
        this.container.appendChild(header);
    }

    initRobots() {
        this.robots.forEach(robot => {
            const robotCard = document.createElement("div");
            robotCard.innerHTML = `
                <img src="${robot.image}" alt="${robot.username}">
                <h2>${robot.name}<span>${robot.username}</span></h2>
                <p><a href="mailto:${robot.email}">${robot.email}</a></p>
            `;
            robotCard.classList.add("roboGameCard");
            this.container.appendChild(robotCard);
        })
    }

    constructor() {
        this.robots = [
            {
                id: 1,
                name: 'Leanne Graham',
                username: 'Bret',
                email: 'Sincere@april.biz',
                image: 'https://robohash.org/1?200x200'
            },
            {
                id: 2,
                name: 'Ervin Howell',
                username: 'Antonette',
                email: 'Shanna@melissa.tv',
                image: 'https://robohash.org/2?200x200'
            },
            {
                id: 3,
                name: 'Clementine Bauch',
                username: 'Samantha',
                email: 'Nathan@yesenia.net',
                image: 'https://robohash.org/3?200x200'
            },
            {
                id: 4,
                name: 'Patricia Lebsack',
                username: 'Karianne',
                email: 'Julianne.OConner@kory.org',
                image: 'https://robohash.org/4?200x200'
            },
            {
                id: 5,
                name: 'Chelsey Dietrich',
                username: 'Kamren',
                email: 'Lucio_Hettinger@annie.ca',
                image: 'https://robohash.org/5?200x200'
            },
            {
                id: 6,
                name: 'Mrs. Dennis Schulist',
                username: 'Leopoldo_Corkery',
                email: 'Karley_Dach@jasper.info',
                image: 'https://robohash.org/6?200x200'
            },
            {
                id: 7,
                name: 'Kurtis Weissnat',
                username: 'Elwyn.Skiles',
                email: 'Telly.Hoeger@billy.biz',
                image: 'https://robohash.org/7?200x200'
            },
            {
                id: 8,
                name: 'Nicholas Runolfsdottir V',
                username: 'Maxime_Nienow',
                email: 'Sherwood@rosamond.me',
                image: 'https://robohash.org/8?200x200'
            },
            {
                id: 9,
                name: 'Glenna Reichert',
                username: 'Delphine',
                email: 'Chaim_McDermott@dana.io',
                image:'https://robohash.org/9?200x200'
            },
            {
                id: 10,
                name: 'Clementina DuBuque',
                username: 'Moriah.Stanton',
                email: 'Rey.Padberg@karina.biz',
                image:'https://robohash.org/10?200x200'
            }
        ];
        this.container = document.querySelector(".roboGame");
        this.hiddenClass = "hidden";
        this.initHeader();
        this.initRobots();
    }
}

new roboGame()