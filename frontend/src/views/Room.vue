<template>
  <div id="Room">
    <div class="room-head">
      <router-link
        :to="{path: '/LessonList',
      query: {
        identity: identity,
        name: studentName,
        id: studentId
      }}"
        class="room-exit"
      >返回房间列表</router-link>
      <div class="class-info">
        <span>课程名称：</span>
        <span class="class-name">{{lessonName}}</span>
        <span>ID：</span>
        <span>{{lessonId}}</span>
      </div>
      <div class="room-name">
        <span>{{studentName}}</span>
      </div>
    </div>
    <div class="room-body">
      <white-board
        class="room-white-board"
        :lessonName="lessonName"
        v-show="isWhiteBoardOrCodeEditor"
      ></white-board>
      <code-editor
        class="room-code-editor"
        :lessonName="lessonName"
        :lessonId="lessonId"
        v-show="!isWhiteBoardOrCodeEditor"
      ></code-editor>
      <el-button round class="room-switch" @click="checkSwitch">切换到{{editorSwitch}}</el-button>
      <webcast class="room-webcast" :identity="identity" :lessonId="lessonId"></webcast>
      <line-list
        :identity="identity"
        :studentName="studentName"
        :lessonId="lessonId"
        :studentId="studentId"
        class="room-line-list"
      ></line-list>
      <chat-box :personId="studentId" :studentName="studentName" :lessonId="lessonId" class="room-chat-box"></chat-box>
    </div>
  </div>
</template>

<script>
import LineList from "../components/LineList";
import CodeEditor from "../components/CodeEditor";
import WhiteBoard from "../components/WhiteBoard";
import ChatBox from "../components/ChatBox";
import Webcast from "../components/Webcast";

export default {
  name: "Room",
  components: {
    LineList,
    CodeEditor,
    WhiteBoard,
    ChatBox,
    Webcast,
  },
  data: function () {
    return {
      isWhiteBoardOrCodeEditor: true,
      editorSwitch: "代码编辑器",
      identity: "",
      studentName: "",
      studentId: "",
      lessonId: "",
      lessonName: "",
    };
  },
  methods: {
    checkSwitch: function () {
      this.isWhiteBoardOrCodeEditor = !this.isWhiteBoardOrCodeEditor;
      if (this.editorSwitch === "白板") this.editorSwitch = "代码编辑器";
      else if (this.editorSwitch === "代码编辑器") this.editorSwitch = "白板";
    },
  },
  created: function () {
    const identity = this.$route.query["identity"];
    const id = this.$route.query["id"];
    const name = this.$route.query["name"];
    const lessonId = this.$route.query["lessonId"];
    const lessonName = this.$route.query["lessonName"];
    this.identity = identity;
    this.studentId = id;
    this.studentName = name;
    this.lessonId = lessonId;
    this.lessonName = lessonName;
  },
};
</script>

<style>
#Room {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: rgba(0, 0, 0, 0);
  text-align: center;
  position: relative;
  margin: 0;
}
.room-head {
  width: 1910px;
  height: 50px;
  background-color: rgba(255, 255, 255, 0.95);
  border-bottom-style: solid;
  border-bottom-width: 1px;
  border-bottom-color: rgb(220, 223, 230);
}
.room-exit {
  float: left;
  line-height: 50px;
  margin: 0 20px;
  color: black;
}
.class-info {
  display: inline;
  line-height: 45px;
}
.class-name {
  display: inline;
  margin-right: 30px;
}
.room-name {
  float: right;
  line-height: 50px;
  margin: 0 20px;
}
.room-body {
  position: relative;
}
.room-switch {
  position: absolute;
  top: 6px;
  left: 6px;
  line-height: 30px;
  font-size: 15px;
  width: 150px;
}
.room-webcast {
  position: absolute;
  top: 0;
  left: 1250px;
}
.room-line-list {
  position: absolute;
  left: 1250px;
  top: 252px;
}
.room-chat-box {
  position: absolute;
  top: 0;
  left: 1550px;
}
a.room-exit:hover {
  color: rgb(255, 150, 0);
}
.router-link-active {
  color: sandybrown;
}
</style>
