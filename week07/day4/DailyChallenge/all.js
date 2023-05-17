async function logJSONData() {
    try {
        const response = await fetch("https://api.le-systeme-solaire.net/rest/bodies/?filter[]=isPlanet,eq,true");
        const jsonData = await response.json();
        return jsonData;
    }
    catch (error) {
        console.warn("Error", error);
        throw error;
    }
}

function addPlanet(planet) {

    const planetColors = {
        "Mercury": "radial-gradient(#ccc, #413f40)",
        "Venus": "radial-gradient(#ad795c, #8a3e14)",
        "Earth": "radial-gradient(#4f701f, #0a5942)",
        "Mars": "radial-gradient(#a4280f, #7e1d09)",
        "Jupiter": "radial-gradient(#a16b35, #7d4b19)",
        "Saturn": "radial-gradient(#6a6551, #4e4625)",
        "Uranus": "radial-gradient(#3b6d90, #1a4360)",
        "Neptune": "radial-gradient(#5293d6, #1c5289)"
    }

    const planetDiv = document.createElement("div");
    const planetInnerDiv = document.createElement("div");
    planetDiv.classList.add("planet");
    const diameter = Math.round(planet['perihelion']**.22)
    planetDiv.style.width = diameter+"vh";
    planetDiv.style.height = diameter+"vh";
    planetDiv.style.animationDuration = Math.round(planet['meanRadius']/1200)+"s";
    planetDiv.style.animationDelay = planet['density']+"s";
    const planetDiameter = Math.round(planet['meanRadius']**.44);
    planetInnerDiv.style.width = planetDiameter +"px";
    planetInnerDiv.style.height = planetDiameter +"px";
    planetInnerDiv.style.margin = Math.round(diameter/8 - planetDiameter/40)+"vh";
    planetInnerDiv.style.background = planetColors[planet['englishName']];
    planetDiv.appendChild(planetInnerDiv);
    document.querySelector(".listPlanets").appendChild(planetDiv);
    if (planet['moons']) {
        for (const moon of planet['moons']) {
            addMoon(moon, planetInnerDiv);
        }
    }
}

function addMoon(moon, holder) {
    const moonDiv = document.createElement("span");
    moonDiv.classList.add("moon");
    holder.appendChild(moonDiv);
}

function implementPlanets(planets) {
    for (const planet of planets['bodies']) {
        addPlanet(planet);
    }
}


logJSONData().then(fetchedData => {
    implementPlanets(fetchedData)
});