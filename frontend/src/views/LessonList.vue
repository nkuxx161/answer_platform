<template>
  <el-container class="lesson-List" id="lessonList">
    <el-header class="header" id="header" height="90px">
      <div class="space" id="space">{{name}}你好：</div>
      <div class="exit" id="exit">
        <router-link to="/Login" class="exit-router">返回</router-link>
      </div>
    </el-header>
    <el-container>
      <el-aside class="calendar" id="calendar">
        <el-row class="tac">
          <el-col :span="12" class="col">
            <el-menu default-active="1" class="el-menu-vertical-demo">
              <el-menu-item index="1" class="menu" @click="getLesson">
                <i class="el-icon-menu"></i>
                <span slot="title">答疑课程</span>
              </el-menu-item>
              <el-menu-item index="2" class="menu" @click="getInformation">
                <i class="el-icon-document"></i>
                <span slot="title">个人信息</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-calendar v-model="value"></el-calendar>
        </el-row>
      </el-aside>
      <el-main class="list" id="list">
        <div class="show-room" v-if="!informationVisible">
          <div class="lesson-room" id="lessonRoom" v-for="(item,key) in lessonList" :key="key">
            <div class="lesson-name" id="lessonName">{{item.lessonName}}</div>
            <div class="lesson-notice" id="lessonNotice">
              <span>本课程公告:</span>
              <br />
              <span id="notice">{{item.lessonNotice}}</span>
            </div>
            <div class="button1" id="Button1">
              <router-link
                :to="{path: '/Room',
                query: {
                  identity: identity,
                  name: name,
                  id: id,
                  lessonName: item.lessonName,
                  lessonId: item.lessonId
                }}"
              >
                <el-button
                  class="in-class"
                  type="primary"
                  @click="goLive(item.lessonId,item.lessonName)"
                >进入直播</el-button>
              </router-link>
            </div>
            <div class="button2" v-if="isTeacher">
              <el-button
                class="change-note"
                type="primary"
                @click="beforeChangeNotice(item.lessonNotice)"
              >编辑公告</el-button>
              <el-dialog
                title="编辑公告"
                :visible.sync="dialogVisible"
                width="30%"
                custom-class="dialog"
              >
                <el-input
                  type="textarea"
                  :autosize="{ minRows: 2, maxRows: 4}"
                  placeholder="请输入内容"
                  v-model="lessonNotice"
                ></el-input>
                <span slot="footer" class="dialog-footer">
                  <el-button @click="quitChangeNotice">取 消</el-button>
                  <el-button type="primary" @click="changeNotice(item.lessonId)">保 存</el-button>
                </span>
              </el-dialog>
            </div>
          </div>
        </div>
        <div class="information" v-if="informationVisible">
          <el-form ref="form" :model="form" label-width="100px">
            <el-form-item label="Name">
              <el-input v-model="name" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="Identity">
              <el-input v-model="identity" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="Id">
              <el-input v-model="id" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="LoginName">
              <el-input v-model="loginName" :disabled="true"></el-input>
            </el-form-item>
            <el-button type="primary" @click="passwordDialogVisible = true">修改密码</el-button>
            <el-dialog
              title="请输入新密码"
              :visible.sync="passwordDialogVisible"
              width="30%"
              :before-close="handleClose"
            >
              <el-input v-model="newPassword"></el-input>
              <span slot="footer" class="dialog-footer">
                <el-button @click="passwordDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="changePassword">确 定</el-button>
              </span>
            </el-dialog>
          </el-form>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: "LessonList",
  data: function () {
    return {
      value: new Date(),
      isTeacher: true,
      identity: "",
      id: "",
      name: "",
      loginName: "",
      newPassword: "",
      lessonList: "",
      lessonNotice: "",
      dialogVisible: false,
      passwordDialogVisible: false,
      informationVisible: false,
    };
  },
  methods: {
    getLesson: function () {
      this.informationVisible = false;
    },
    getInformation: function () {
      this.informationVisible = true;
    },
    getStudentLessonList: function () {
      this.$axios
        .post("student/checkLesson/", { studentId: this.id })
        .then((response) => {
          this.lessonList = response.data;
        });
    },
    getTeacherLessonList: function () {
      this.$axios
        .post("teacher/checkLesson/", { teacherId: this.id })
        .then((response) => {
          this.lessonList = response.data;
        });
    },
    beforeChangeNotice: function (lessonNotice) {
      this.dialogVisible = true;
      this.lessonNotice = lessonNotice;
    },
    quitChangeNotice: function () {
      this.dialogVisible = false;
    },
    changeNotice: function (lessonId) {
      this.$axios
        .post("lesson/changeNotice/", {
          lessonId: lessonId,
          lessonNotice: this.lessonNotice,
        })
        .then(() => {
          this.getTeacherLessonList();
          this.dialogVisible = false;
        });
    },
    changePassword: function () {
      this.passwordDialogVisible = false;
      if (this.newPassword === "") {
        alert("密码不能为空");
      } else {
        if (this.isTeacher) {
          this.$axios
            .post("teacher/changePassword/", {
              teacherId: this.id,
              teacherPassword: this.newPassword,
            })
            .then((response) => {
              if (response.data.code === "true") {
                alert("修改成功");
                this.newPassword = ""
              } else {
                alert("修改失败");
              }
            });
        } else {
          this.$axios
            .post("student/changePassword/", {
              studentId: this.id,
              studentPassword: this.newPassword,
            })
            .then((response) => {
              if (response.data.code === "true") {
                alert("修改成功");
              } else {
                alert("修改失败");
              }
            });
        }
      }
    },
    goLive: function (lessonId, lessonName) {
      if (this.isTeacher) {
        this.$router.push({
          path: "/Room",
          query: {
            identity: this.identity,
            id: this.id,
            name: this.name,
            lessonId: lessonId,
            lessonName: lessonName,
          },
        });
      } else {
        this.$router.push({
          path: "/Room",
          query: {
            identity: this.identity,
            id: this.id,
            name: this.name,
            lessonId: lessonId,
            lessonName: lessonName,
          },
        });
      }
    },
  },
  mounted: function () {
    const identity = this.$route.query["identity"];
    const id = this.$route.query["id"];
    const name = this.$route.query["name"];
    const loginName = this.$route.query["loginName"];
    if (identity === "student") {
      this.isTeacher = false;
      this.identity = "student";
      this.id = id;
      this.name = name;
      this.loginName = loginName;
    } else {
      this.isTeacher = true;
      this.identity = "teacher";
      this.id = id;
      this.name = name;
      this.loginName = loginName;
    }
    if (!this.isTeacher) {
      this.getStudentLessonList();
    } else {
      this.getTeacherLessonList();
    }
  },
};
</script>

<style scoped>
.lesson-list {
  display: flex;
  flex-wrap: wrap;
  margin-top: 0;
  background-color: #ffffff;
}
.list {
  flex: 8 1 200px;
  min-width: 600px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-content: flex-start;
}
.show-room {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-content: flex-start;
}
.information {
  position: relative;
  top: 20%;
  width: 30%;
  padding: 10px;
  border: #dcdcdc 1px solid;
}
.calendar {
  flex: 1 1 230px;
  margin-top: 0;
  background-color: #f2f8fe;
}
.tac {
  border-right: #dcdcdc 1px solid;
}
.col {
  width: 100%;
  height: 150px;
}
.menu {
  height: 75px;
  padding-top: 10px;
}
.header {
  margin-top: 0;
  font-family: "宋体";
  width: 100%;
  background-color: #409eff;
}
.space {
  float: left;
  font-size: 22px;
  color: #ffffff;
  line-height: 90px;
  margin-left: -300px;
  width: 40%;
}
.exit {
  float: right;
  font-size: 20px;
  line-height: 90px;
  margin-right: 50px;
}
.exit-router {
  color: #ffffff;
}
.exit-router:hover {
  color: #ff0000;
}
.lesson-room {
  margin-top: 20px;
  font-family: "宋体";
  width: 80%;
  height: 120px;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  background-color: #ffffff;
  border-radius: 10px;
  border: #000000 1px solid;
}
.lesson-room:hover {
  box-shadow: 3px 3px 10px #bebebe;
  border: #000000 1px solid;
}
.lesson-name {
  float: left;
  font-size: 30px;
  line-height: 98px;
  text-align: center;
  width: 30%;
  height: 100%;
  border-right: #000000 2px solid;
}
.lesson-notice {
  float: left;
  text-align: left;
  font-size: 20px;
  padding-left: 10px;
  padding-top: 10px;
  width: 50%;
  height: 92%;
  border-right: #000000 2px solid;
}
#notice {
  display: block;
  text-indent: 2em;
}
.button1 {
  width: 15%;
  height: 50%;
  float: left;
}
.button2 {
  width: 15%;
  height: 50%;
  float: left;
}
.in-class {
  position: relative;
  top: 10%;
  height: 80%;
  min-width: 65px;
  margin-left: 15%;
}
.change-note {
  position: relative;
  top: 10%;
  height: 80%;
  min-width: 65px;
  margin-left: 15%;
}
.dialog {
  border-radius: 50px;
}
</style>
