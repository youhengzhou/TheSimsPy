const WebSocket = require("ws");

function setupWebSocket(server) {
  const wss = new WebSocket.Server({ noServer: true });

  server.on("upgrade", function upgrade(request, socket, head) {
    try {
      // authentication and other steps
      wss.handleUpgrade(request, socket, head, function done(ws) {
        wss.emit("connection", ws, request);
      });
    } catch (err) {
      console.log("upgrade exception", err);
      socket.write("HTTP/1.1 401 Unauthorized\r\n\r\n");
      socket.destroy();
      return;
    }
  });

  wss.on("connection", (ctx) => {
    console.log("connected", wss.clients.size);

    ctx.on("message", (message) => {
      console.log(`Received message => ${message}`);
      ctx.send(`you said ${message}`);
    });

    ctx.on("close", () => {
      console.log("closed", wss.clients.size);
    });

    ctx.send("connection established.");
  });
}

module.exports = setupWebSocket;
