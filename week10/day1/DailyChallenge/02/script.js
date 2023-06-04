const {largeNumber} = require("../01/main")

let http = require("http");
const server = http.createServer( (req, res) => {
    res.setHeader('Content-Type', 'text/html');
    res.writeHead(200);
    res.end(`
        <h1>Hi there at the frontend</h1>
        <p>My Module is ${largeNumber + 6}</p>
    `);
    console.log('I am listening....');
});
server.listen(3000);
