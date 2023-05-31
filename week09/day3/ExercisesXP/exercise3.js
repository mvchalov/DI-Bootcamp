// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));

(async ()=>{
    try {
        const responce = await fetch("https://www.swapi.tech/api/starships/9/");
        const data = await responce.json();
        console.log(data.result.properties)
    }
    catch (e) {
        console.error(e, "has occurred")
    }
})()