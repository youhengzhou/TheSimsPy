const axios = require("axios");
const express = require("express");
const cors = require("cors");
const app = express();
const http = require("http");
const server = require("http").createServer(app);
const WebSocket = require("ws");

app.use(express.json());
app.use(cors());

const wss = new WebSocket.Server({ server });

wss.on("connection", function connection(ws) {
  ws.on("message", function incoming(message) {
    console.log("received: %s", message);
  });
});

app.get("/wait", async (req, res) => {
  try {
    let time = 0;
    async function sendData() {
      wss.clients.forEach(async (client) => {
        if (client.readyState === WebSocket.OPEN) {
          //   const data = await db.read(req.query.dirname);
          //   const data = await axios.get(req.query.dirname)
          let response = await axios.get(
            "http://localhost:3000/read?dirname=test0"
          );

          //   console.log(data);

          console.log("we are now sending data to client");
          time += 1;
          console.log(time);

          client.send(JSON.stringify(response.data));
        }
      });
    }
    // let i = 0;
    // while (i < 5000000) {
    setInterval(sendData, 1000);
    //   i += 1;
    // }
  } catch (error) {}
});

server.listen(9000, () => console.log("The websocket on port 9000"));

app.listen(9001, () =>
  console.log("The jsoneng API wrapper is running on port 9001")
);
