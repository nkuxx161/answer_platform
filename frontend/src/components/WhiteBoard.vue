<template>
  <div id="board" @mousemove="isMouseOut($event)">
    <canvas
      id="whiteBoardCanvas"
      @mousedown="canvasDown($event)"
      @mouseup="canvasUp()"
      @mousemove="canvasMove($event)"
      width="1000"
      height="820"
      style="border:1px solid #c3c3c3"
    ></canvas>
    <el-card class="pen-color">
      <div slot="header" class="pen-color-title">画笔颜色</div>
      <el-button
        class="pen-color-button"
        v-for="item in colors"
        :key="item"
        :style="{ background: item }"
        @click="setColor(item)"
      ></el-button>
    </el-card>
    <el-card class="pen-width">
      <div slot="header" class="pen-width-title">画笔大小</div>
      <el-button
        size="medium"
        class="pen-width-button"
        v-for="pen in brushs"
        :key="pen.width"
        @click="setWidth(pen.lineWidth)"
      >{{pen.name}}</el-button>
    </el-card>
    <el-card class="white-board-function">
      <div slot="header" class="white-board-function-title">画笔功能</div>
      <el-button round class="white-board-function-title-button" @click="penCanvas()">笔</el-button>
      <el-button round class="white-board-function-title-button" @click="eraserCanvas()">橡皮</el-button>
      <el-button round class="white-board-function-title-button" @click="previousCanvas()">撤销</el-button>
      <el-button round class="white-board-function-title-button" @click="nextCanvas()">还原</el-button>
      <el-button round class="white-board-function-title-button" @click="clearAllCanvas()">清除</el-button>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "whiteboard",
  props: {
    lessonName: {
      type: String,
    },
  },
  data: function () {
    return {
      socketId: "",
      colors: [
        "#fef4ac",
        "#0018ba",
        "#ffc200",
        "#f32f15",
        "#000000",
        "#5ab639",
      ],
      brushs: [
        {
          name: "3号",
          lineWidth: 3,
        },
        {
          name: "6号",
          lineWidth: 6,
        },
        {
          name: "12号",
          lineWidth: 12,
        },
        {
          name: "24号",
          lineWidth: 24,
        },
      ],
      context: {},
      canvasMoveUse: false,
      initializationConfig: {
        lineWidth: 4,
        lineColor: "#000000",
        shadowBlur: 2,
      },
      preCanvasArray: [], //保存上一步的数组
      midCanvasArray: [], //保存当前状态
      nextCanvasArray: [], //保存撤回后的下一步数组
    };
  },
  sockets: {},
  created() {
    //初始化时用于接收socket唯一id标识
    this.sockets.listener.subscribe("getSocketId", (data) => {
      this.socketId = data;
    });

    this.sockets.listener.subscribe("mountCanvas", (data) => {
      const whiteBoardCanvas = document.getElementById("whiteBoardCanvas");
      let url = whiteBoardCanvas.toDataURL("image/png");
      this.$socket.emit("drawCanvas", {
        url: url,
        socketId: data.socketId,
      });
    });

    this.sockets.listener.subscribe("drawPaint", (data) => {
      let newImage = new Image();
      newImage.onload = function () {
        let whiteBoardCanvas = document.getElementById("whiteBoardCanvas");
        let ctx = whiteBoardCanvas.getContext("2d");
        ctx.clearRect(0, 0, 1200, 820);
        ctx.drawImage(newImage, 0, 0);
      };
      newImage.src = data;
    });

    //用于监听其他房间发出的mousedown信息
    this.sockets.listener.subscribe("downPaint", (data) => {
      this.context.beginPath();
      this.context.moveTo(data.canvasX, data.canvasY);
    });

    //用于监听其他房间发出的mousemove信息
    this.sockets.listener.subscribe("movePaint", (data) => {
      this.context.lineTo(data.moveCanvasX, data.moveCanvasY);
      this.context.stroke();
    });

    //用于监听其他房间发出的橡皮擦按钮信息
    this.sockets.listener.subscribe("eraserGet", () => {
      this.context.lineWidth = 40;
      this.context.shadowBlur = 2;
      this.context.shadowColor = "#ffffff";
      this.context.strokeStyle = "#ffffff";
    });

    //用于监听其他房间发出的笔按钮信息
    this.sockets.listener.subscribe("penGet", () => {
      this.setCanvasStyle();
    });

    this.sockets.listener.subscribe("setWidthGet", (data) => {
      this.context.lineWidth = data;
    });

    this.sockets.listener.subscribe("setColorGet", (data) => {
      this.context.strokeStyle = data;
      this.context.shadowColor = data;
    });

    this.sockets.listener.subscribe("clearGet", () => {
      let c = document.getElementById("whiteBoardCanvas");
      let context = c.getContext("2d");
      context.clearRect(0, 0, 1200, 820);
    });

    this.sockets.listener.subscribe("changeCanvas", (data) => {
      this.$socket.emit("getCanvas", data);
    });

    this.sockets.listener.subscribe("sendCanvas", (data) => {
      const whiteBoardCanvas = document.getElementById("whiteBoardCanvas");
      let url = whiteBoardCanvas.toDataURL("image/png");
      this.$socket.emit("updateCanvas", {
        url: url,
        lessonName: data,
      });
    });

    this.$socket.emit("joinRoom", this.lessonName);
    this.$socket.emit("sendSocketId");
  },
  mounted() {
    const whiteBoardCanvas = document.getElementById("whiteBoardCanvas");
    this.context = whiteBoardCanvas.getContext("2d");
    this.initCanvas();
    this.setCanvasStyle();
    this.$socket.emit("mountCanvas", {
      lessonName: this.lessonName,
      socketId: this.socketId,
    });
  },
  beforeDestroy() {
    this.$socket.emit("leaveRoom", this.lessonName);
  },
  methods: {
    initCanvas() {
      //初始化绘制信息
      let initStatus = this.context.getImageData(0, 0, 1000, 850);
      this.midCanvasArray.push(initStatus);
    },
    setCanvasStyle() {
      this.context.lineWidth = this.initializationConfig.lineWidth;
      this.context.shadowBlur = this.initializationConfig.shadowBlur;
      this.context.shadowColor = this.initializationConfig.lineColor;
      this.context.strokeStyle = this.initializationConfig.lineColor;
    },
    isMouseOut(e) {
      const whiteBoardCanvas = document.getElementById("whiteBoardCanvas");
      if (e.target !== whiteBoardCanvas) {
        this.canvasMoveUse = false;
      }
    },
    canvasUp() {
      let preCanvas = this.context.getImageData(0, 0, 1000, 820);
      this.midCanvasArray[0] = preCanvas;
      if (this.nextCanvasArray.length) {
        this.nextCanvasArray = [];
      }
      this.canvasMoveUse = false;
    },
    canvasMove(e) {
      if (this.canvasMoveUse) {
        const t = e.target;
        let moveCanvasX;
        let moveCanvasY;
        moveCanvasX = e.clientX - t.parentNode.offsetLeft;
        moveCanvasY = e.clientY - t.parentNode.offsetTop - 50;
        this.context.lineTo(moveCanvasX, moveCanvasY);
        this.$socket.emit("mouseMove", {
          moveCanvasX: moveCanvasX,
          moveCanvasY: moveCanvasY,
          lessonName: this.lessonName,
        });
        this.context.stroke();
      }
    },
    canvasDown(e) {
      this.canvasMoveUse = true;
      const canvasX = e.clientX - e.target.parentNode.offsetLeft;
      const canvasY = e.clientY - e.target.parentNode.offsetTop - 50;
      this.context.beginPath();
      this.context.moveTo(canvasX, canvasY);
      let preCanvas = this.context.getImageData(0, 0, 1000, 810);
      this.preCanvasArray.push(preCanvas);
      this.$socket.emit("mouseDown", {
        canvasX: canvasX,
        canvasY: canvasY,
        lessonName: this.lessonName,
      });
    },
    clearAllCanvas() {
      let preCanvas = this.context.getImageData(0, 0, 1000, 820);
      this.preCanvasArray.push(preCanvas);
      let c = document.getElementById("whiteBoardCanvas");
      let context = c.getContext("2d");
      context.clearRect(0, 0, 1200, 820);
      let currentCanvas = this.context.getImageData(0, 0, 1000, 820);
      this.midCanvasArray[0] = currentCanvas;
      this.$socket.emit("clearEmit", this.lessonName);
    },
    previousCanvas() {
      if (this.preCanvasArray.length) {
        let preCanvas = this.preCanvasArray.pop();
        let currentCanvas = this.midCanvasArray[0];
        this.midCanvasArray[0] = preCanvas;
        this.nextCanvasArray.push(currentCanvas);
        this.context.putImageData(preCanvas, 0, 0);
        this.$socket.emit("changeCanvas", {
          lessonName: this.lessonName,
          socketId: this.socketId,
        });
      }
    },
    nextCanvas() {
      if (this.nextCanvasArray.length) {
        let nextCanvas = this.nextCanvasArray.pop();
        let currentCanvas = this.midCanvasArray[0];
        this.preCanvasArray.push(currentCanvas);
        this.midCanvasArray[0] = nextCanvas;
        this.context.putImageData(nextCanvas, 0, 0);
        this.$socket.emit("changeCanvas", {
          lessonName: this.lessonName,
          socketId: this.socketId,
        });
      }
    },
    eraserCanvas() {
      this.context.lineWidth = 40;
      this.context.shadowBlur = 2;
      this.context.shadowColor = "#ffffff";
      this.context.strokeStyle = "#ffffff";
      this.$socket.emit("eraserEmit", this.lessonName);
    },
    penCanvas() {
      this.setCanvasStyle();
      this.$socket.emit("penEmit", this.lessonName);
    },
    setColor(color) {
      this.context.strokeStyle = color;
      this.context.shadowColor = color;
      this.$socket.emit("setColorEmit", {
        color: color,
        lessonName: this.lessonName,
      });
    },
    setWidth(width) {
      this.context.lineWidth = width;
      this.$socket.emit("setWidthEmit", {
        width: width,
        lessonName: this.lessonName,
      });
    },
  },
};
</script>

<style scoped>
#board {
  position: relative;
  margin: 100px auto 100px auto;
  width: 1250px;
  height: 822px;
  background-color: #f2e6e6;
  border-radius: 10px;
  margin: 10px 0;
  /* overflow: hidden; */
}
#whiteBoardCanvas {
  position: absolute;
  top: 0;
  left: 0;
  height: 820px;
  margin-bottom: 10px;
  width: 1000px;
  border-radius: 10px 0 0 10px;
  background-color: #ffffff;
}
.pen-color {
  position: absolute;
  left: 1000px;
  top: 0px;
  border: solid 1px rgb(195, 195, 195);
  border-radius: 0 10px 0 0;
}
.pen-color-title {
  margin: 0;
  font-size: 20px;
  color: #000000;
  font-family: "楷体";
  font-size: 23px;
}
.pen-color-button {
  margin: 10px;
}
.pen-width {
  position: absolute;
  left: 1000px;
  top: 197px;
  border: solid 1px rgb(195, 195, 195);
  border-radius: 0;
  /* border-radius: 10px; */
}
.pen-width-title {
  margin: 0;
  font-size: 20px;
  color: #000000;
  font-family: "楷体";
  font-size: 23px;
}
.pen-width-button {
  width: 80px;
  font-size: 18px;
  margin: 20px 10px;
}
.white-board-function {
  position: absolute;
  left: 1000px;
  top: 462px;
  border: solid 1px rgb(195, 195, 195);
  border-radius: 0 0 10px 0;
}
.white-board-function-title {
  margin: 0;
  font-size: 20px;
  color: #000000;
  height: 29px;
  font-family: "楷体";
  font-size: 23px;
}
.white-board-function-title-button {
  width: 80px;
  font-size: 18px;
  margin: 20px 10px;
}
</style>
