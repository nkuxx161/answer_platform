<template>
  <div class="backgroud">
    <h1>登录</h1>
    <div class="which">
      <span class="who">身份：</span>
      <div class="student">
        <input @click="studentLogin" type="radio" name="people" value="student">
        学生
      </div>
      <div class="teacher">
        <input @click="teacherLogin" type="radio" name="people" value="teacher">
        老师
      </div>
      <div class="admin">
        <input @click="adminLogin" type="radio" name="people" value="admin">
        管理员
      </div>
    </div>
    <div class="name">
      账号：
      <input v-model="loginName" type="text" name="name" class="in-name">
    </div>
    <div class="password">
      密码：
      <input v-model="password" type="password" name="password" class="in-pass">
    </div>
    <div class="box">
      <el-button type="primary" class="login" @click="login">
        登录
      </el-button>
      <router-link to="/">
        <el-button type="primary" class="back">
        返回
        </el-button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: function () {
    return {
      loginName: '',
      password: '',
      identity: 'student',
    }
  },

  methods: {
    initialDate: function () {
      this.loginName = ""
      this.password = ""
    },
    studentLogin: function () {
      this.identity = "student"
    },

    teacherLogin: function () {
      this.identity = "teacher"
    },

    adminLogin: function () {
      this.identity = "admin"
    },

    login: function () {
      if (this.identity === "student") {
        this.$axios.post('student/login/', {
          studentEmail: this.loginName,
          studentPassword: this.password
        }).then((response) => {
          if (response.data.code === "true") {
            this.$alert('登录成功')
            this.$router.push({
              path: '/LessonList',
              query: {
                identity: this.identity,
                id: response.data.studentInfor['studentId'],
                name: response.data.studentInfor['studentName'],
                loginName: this.loginName
              }
            })
          } else {
            this.$alert('登录失败')
            this.initialDate()
          }
        })
      }
      if (this.identity === "teacher") {
        this.$axios.post('teacher/login/', {
          teacherEmail: this.loginName,
          teacherPassword: this.password
        }).then((response) => {
          if (response.data.code === "true") {
            this.$alert('登录成功')
            this.$router.push({
              path: '/LessonList',
              query: {
                identity: this.identity,
                id: response.data.teacherInfor['teacherId'],
                name: response.data.teacherInfor['teacherName'],
                loginName: this.loginName
              }
            })
          } else {
            this.$alert('登录失败')
            this.initialDate()
          }
        })
      }
      if (this.identity === "admin") {
        this.$axios.post('teachingAdmin/login/', {
          adminName: this.loginName,
          adminPassword: this.password
        }).then((response) => {
          if (response.data.code === "true") {
            this.$alert('登录成功')
            this.$router.push({
              path: '/Backstage',
              query: {
                adminName: this.loginName
              }
            })
          } else {
            this.$alert('登录失败')
            this.initialDate()
          }
        })
      }
    }
  }
}
</script>

<style scoped>
body {
  margin: 0;
}
.backgroud {
  background-color: #409EFF;;
  width: 700px;
  height: 450px;
  margin-right: auto;
  margin-left: auto;
  border-radius: 30px;
  margin-top: 150px;
}
h1 {
  padding-top: 50px;
  font-size: 50px;
  padding-bottom: 10px;
  margin-bottom: 0px;
  margin-left: 0;
  color: #fff;
}
.name {
  width: 700px;
  height: 80px;
  font-size: 20px;
  margin-left: -30px;
  color: #fff;
}
.password {
  width: 700px;
  height: 80px;
  font-size: 20px;
  margin-left: -30px;
  color: #fff;
}
.in-name {
  width: 300px;
  height: 30px;
  border-radius: 12px;
}
.in-pass {
  width: 300px;
  height: 30px;
  border-radius: 12px;
}
.box {
  width: 700px;
  height: 80px;
}
.login {
  float: left;
  width: 90px;
  height: 40px;
  font-size: 20px;
  margin-left: 200px;
  background-color: #fff;
  color: #409EFF;
  border-radius: 15px;
}
.back {
  float: right;
  width: 90px;
  height: 40px;
  font-size: 20px;
  margin-right: 200px;
  background-color: #fff;
  color: #409EFF;
  border-radius: 15px;
}
.which {
  font-size: 21px;
  width: 700px;
  margin-top: 10px;
  margin-bottom: 40px;
}
.who {
  margin-right: -122px;
  color: #fff;
}
.student {
  float: right;
  margin-right: 200px;
  color: #fff;
}
.teacher {
  float: right;
  margin-right: 35px;
  color: #fff;
}
.admin {
  float: right;
  margin-right: 30px;
  color: #fff;
}
</style>
