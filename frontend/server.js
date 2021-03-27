//HTTP

let http = require("http");
let path = require("path");

let fs = require("fs");

let server = http.createServer(handleRequest)
server.listen(8080);

function handleRequest(req, res) {
  let pathname = req.url;

  if (pathname == "/") {
    pathname = "/src/views/Room.vue";
  }

  let ext = path.extname(pathname);

  //Mnap extension to file type
  let typeExt = {
    ".html": "text/html",
    ".js": "text/jaavascript",
    ".css": "text/css",
    ".vue": "text/vue"
  }

  let contentType = typeExt[ext] || "text/plain"

  fs.readFile(__dirname + pathname, (err, data) => {
    if (err) {
      res.writeHead(500);
      return res.end("Error loading" + pathname)
    }

    //Oteherwise,send data back
    res.writeHead(200, { "Content-Type": contentType });
    res.end(data);
  })
}

//Websocket
let io = require("socket.io").listen(server)

io.sockets.on("connection", (socket) => {
  socket.on("joinRoom", (data) => {
    socket.join(data)
  });

  socket.on("sendSocketId", () => {
    socket.emit("getSocketId",socket.id)
  });

  socket.on("mountCanvas", (data) => {
    socket.broadcast.to(data.lessonName).emit("mountCanvas",
    {
      lessonName: data.lessonName,
      socketId: socket.id
    })
  });

  socket.on("drawCanvas", (data) => {
    socket.broadcast.to(data.socketId).emit("drawPaint", data.url)
  });

  socket.on("mouseDown", (data) => {
    socket.broadcast.to(data.lessonName).emit("downPaint", data)
  });

  socket.on("mouseMove", (data) => {
    socket.broadcast.to(data.lessonName).emit("movePaint", data)
  });

  socket.on("eraserEmit", (data) => {
    socket.broadcast.to(data).emit("eraserGet")
  });

  socket.on("penEmit", (data) => {
    socket.broadcast.to(data).emit("penGet")
  });

  socket.on("setWidthEmit", (data) => {
    socket.broadcast.to(data.lessonName).emit("setWidthGet",data.width)
  });

  socket.on("setColorEmit", (data) => {
    socket.broadcast.to(data.lessonName).emit("setColorGet",data.color)
  });

  socket.on("clearEmit", (data) => {
    socket.broadcast.to(data).emit("clearGet")
  });

  socket.on("changeCanvas", (data) => {
    socket.broadcast.to(data.lessonName).emit("changeCanvas", data)
  });

  socket.on("getCanvas", (data) => {
    socket.broadcast.to(data.socketId).emit("sendCanvas", data.lessonName)
  });

  socket.on("updateCanvas", (data) => {
    socket.broadcast.to(data.lessonName).emit("drawPaint", data.url)
  });

  socket.on("leaveRoom", (data) => {
    socket.leave(data)
  });

  socket.on("changeContent", (data) => {
    socket.broadcast.emit("getContent", data)
  });

  socket.on("disconnect", () => {
  })


})
