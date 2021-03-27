<template>
  <div id="all">
    <jsk-header header-background-color="#FFF" header-center-width="1200">
      <h1>教务处后台</h1>
      <span class="header-infor" id="adminName">{{adminName}}</span>
      <span class="header-infor">
        <router-link to="/">退出</router-link>
      </span>
    </jsk-header>
    <jsk-container id="container" is-full-screen :container-width="1900" :has-bleed="false">
      <aside id="buttons">
        <jsk-button
          button-background-color="rgb(102,177,255)"
          @click="setCurrentInformation('createRoom')"
        >创建房间</jsk-button>
      </aside>
      <ul id="roomList">
        <li v-for="(room, index) in roomList" :key="index" class="single-room">
          <div>课程名字：{{room.lessonName}}</div>
          <div>课程代号：{{room.lessonId}}</div>
          <div class="notice">课程公告：{{room.lessonNotice}}</div>
          <div class="room-buttons">
            <jsk-button
              button-background-color="rgb(102,177,255)"
              button-type="success"
              button-size="mini"
              @click="changeCurrentRoom(room.lessonId), setCurrentInformation('addTeacher')"
            >添加老师</jsk-button>
            <jsk-button
              button-background-color="rgb(102,177,255)"
              button-type="success"
              button-size="mini"
              @click="changeCurrentRoom(room.lessonId), setCurrentInformation('addStudent')"
            >添加学生</jsk-button>
          </div>
          <div class="room-buttons">
            <jsk-button
              button-background-color="rgb(102,177,255)"
              button-type="success"
              button-size="mini"
              @click="deleteRoom(room.lessonId)"
            >删除房间</jsk-button>
            <jsk-button
              button-background-color="rgb(102,177,255)"
              button-type="success"
              button-size="mini"
              @click="checkInformation(room.lessonId)"
            >查看信息</jsk-button>
          </div>
        </li>
      </ul>
      <div id="roomInformation">
        <create-room @refreshRoomList="getRoomList" v-if="currentInformation === 'createRoom'"></create-room>
        <add-teacher-information
          v-if="currentInformation === 'addTeacher'"
          :parentRoomId="currentRoomId"
        ></add-teacher-information>
        <add-student-information
          v-if="currentInformation === 'addStudent'"
          :parentRoomId="currentRoomId"
        ></add-student-information>
        <people-infor
          ref="child"
          v-if="currentInformation === 'checkInfor'"
          :lessonId="currentRoomId"
        ></people-infor>
      </div>
    </jsk-container>
  </div>
</template>

<script>
import { header, container, button } from "jellies";
import CreateRoom from "../components/BackstageComponents/CreateRoom.vue";
import AddTeacherInformation from "../components/BackstageComponents/AddTeacherInformation.vue";
import AddStudentInformation from "../components/BackstageComponents/AddStudentInformation.vue";
import PeopleInfor from "../components/BackstageComponents/PeopleInformation.vue";

export default {
  name: "Backstage",
  data: function () {
    return {
      adminName: "admin",
      currentRoomId: "",
      currentInformation: "",
      roomList: [],
    };
  },
  components: {
    JskHeader: header,
    JskContainer: container,
    JskButton: button,
    CreateRoom,
    AddTeacherInformation,
    AddStudentInformation,
    PeopleInfor,
  },
  methods: {
    setCurrentInformation: function (displayInformation) {
      this.currentInformation = displayInformation;
    },
    getRoomList: function () {
      this.$axios.get("lesson/").then((response) => {
        this.roomList = response.data;
      });
    },
    changeCurrentRoom: function (lessonId) {
      this.currentRoomId = lessonId;
    },
    deleteRoom: function (roomLessonId) {
      this.$axios
        .post("teachingAdmin/deleteLesson/", {
          lessonId: roomLessonId,
        })
        .then((response) => {
          if (response.data.code === "false") {
            alert("删除房间失败");
          } else {
            alert("删除房间成功");
            this.getRoomList();
            this.setCurrentInformation("");
          }
        });
    },
    checkInformation: function (lessonId) {
      this.changeCurrentRoom(lessonId);
      this.setCurrentInformation("checkInfor");
    },
  },
  mounted: function () {
    this.getRoomList();
    const name = this.$route.query["adminName"];
    this.adminName = name;
  },
};
</script>

<style scopped>
body {
  margin: 0;
}
h1 {
  color: rgb(30, 30, 30);
  line-height: 50px;
  font-size: 30px;
  margin-left: 50px;
}
#all {
  background-color: #fff;
}
#container {
  display: flex;
}
#buttons {
  padding: 5px;
  border-radius: 10px;
  border: 2px solid gray;
  flex-grow: 0;
}
#roomList {
  margin: 0;
  padding: 5px;
  border-radius: 10px;
  list-style: none;
  border: 2px solid gray;
  flex-grow: 0;
  overflow-y: scroll;
}
#roomInformation {
  padding: 10px;
  flex-grow: 5;
  margin: auto 400px;
}
#adminName {
  margin-left: 1500px;
  color: rgb(30, 30, 30);
}
.room-buttons {
  margin: 5px 0;
}
.header-infor {
  margin: 5px;
  line-height: 50px;
  font-size: 20px;
  color: black;
}
.notice {
  width: 180px;
}
.single-room {
  margin: 3px;
  padding: 2px;
  border-radius: 10px;
  border: 2px solid lightgray;
  text-align: center;
}
.single-room:hover {
  background-color: lightskyblue;
}
</style>
