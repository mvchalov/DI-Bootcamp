document.addEventListener("DOMContentLoaded", function() {

    // Scrolling to anchors

    const navLinks = document.querySelectorAll("a");
    for (const link of navLinks) {
        link.addEventListener("click", (event)=>{
            if (event.target.getAttribute("href").indexOf("#")>-1) {
                event.preventDefault();
                const href = event.target.getAttribute("href");
                const offsetTop = document.querySelector(href).offsetTop;
                scroll({
                    top: offsetTop,
                    behavior: "smooth"
                })
            }
        })
    }

    // Accordion at Characters

    const characterLinks = document.querySelectorAll("#characters aside a");
    const characterArticles = document.querySelectorAll("#characters article");
    for (const [i,link] of characterLinks.entries()) {
        link.addEventListener("click", (event)=>{
            event.preventDefault();
            characterLinks.forEach((e,j)=>{
                if (j==i) {
                    e.parentNode.classList.add("active");
                }
                else {
                    e.parentNode.classList.remove("active")
                }
            })
            characterArticles.forEach((e,j)=>{
                if (j==i) {
                    e.classList.add("active");
                }
                else {
                    e.classList.remove("active")
                }
            })
        })
    }

});