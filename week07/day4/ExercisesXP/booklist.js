const allBooks = []

function initABook(title, author, image, alreadyRead) {
    allBooks.push({
        'title': title,
        'author': author,
        'image': image,
        'alreadyRead': alreadyRead
    })
}

initABook("LOTR", "JRRT", "https://www.isfdb.org/wiki/images/6/61/THHBBTTHLR1986.jpg", false);

initABook("Stars my destination", "Alfred Bester", "https://www.isfdb.org/wiki/images/c/ce/THSTRSMDST1979.jpg", true);

allBooks.forEach(e=>{
    let container = document.createElement("div");
    let title = document.createElement("h2");
    title.innerHTML = e['title'];
    container.appendChild(title);
    let author = document.createElement("p");
    author.innerHTML = e['author'];
    container.appendChild(author)
    let image = document.createElement("img");
    image.src = e['image'];
    if (e['alreadyRead']) {
        container.classList.add('read')
    }
    container.appendChild(image);
    document.querySelector(".listBooks").appendChild(container)
})