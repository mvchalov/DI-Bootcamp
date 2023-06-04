let http = require("http");
const {dateAndTime} = require("./main");

const server = http.createServer( (req, res) => {
    res.setHeader('Content-Type', 'text/html');
    res.writeHead(200);
    res.end(`
        <p>The current date and time are ${new Date(dateAndTime).toString()}</p>
    `);
});
server.listen(8080);