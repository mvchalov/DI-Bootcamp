const url = 'https://love-calculator.p.rapidapi.com/getPercentage?sname=Alice&fname=John';
const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': 'cc22bb6f2fmsh82a4f4a7f967484p192ca7jsn5454263ae789',
        'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
    }
};

try {
    const response = fetch(url, options)
        .then(res => res.json())
        .then (data => console.log(data))
}
catch {
    console.log("Error")
}

const urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/albums"
]

const promises = urls.map(e=>fetch(e).then(res => res.json()));
Promise.all(promises)
    .then(res => console.log(res))
    .catch(err => console.log(err))