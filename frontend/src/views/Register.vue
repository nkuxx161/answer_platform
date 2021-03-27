<template>
  <div class="backgroud">
    <h1>注册</h1>
    <div class="which">
      <span class="who">身份：</span>
      <div class="student">
        <input @click="studentRegister" type="radio" name="people" value="student">
        学生
      </div>
      <div class="teacher">
        <input @click="teacherRegister" type="radio" name="people" value="teacher">
        老师
      </div>
    </div>
    <div class="name">
      账号：
      <input v-model="name" type="text" name="name" class="in-name">
    </div>
    <div class="password">
      密码：
      <input v-model="password" type="password" name="password" class="in-pass">
    </div>
    <div class="repeat-password">
      确认密码：
      <input v-model="rePassword" type="password" name="password" class="repeat-in-pass">
    </div>
    <div class="card">
      工号/学号：
      <input v-model="card" type="text" name="card" class="in-card">
    </div>
    <div class="real-name">
      真实姓名：
      <input v-model="relName" type="text" name="relName" class="in-real-name">
    </div>
    <div class="box">
      <el-button type="primary" class="register" @click="register">
        注册
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
  name: 'Register',
  data: function () {
    return {
      name: '',
      password: '',
      rePassword: '',
      card: '',
      relName: '',
      identity: 'student'
    }
  },

  methods: {
    initialDate: function () {
      this.name = ""
      this.password = ""
      this.rePassword = ""
      this.card = ""
      this.relName = ""
    },
    studentRegister: function () {
      this.identity = "student"
    },
    teacherRegister: function () {
      this.identity = "teacher"
    },

    register: function () {
      if (this.identity === "student") {
        if (this.password !== this.rePassword) {
          this.$alert('两次密码不一致')
          this.initialDate()
        } else {
          this.$axios.post('student/register/', {
            studentId: this.card,
            studentName: this.relName,
            studentEmail: this.name,
            studentPassword: this.password
          }).then((response) => {
            if (response.data.code === "true") {
              this.$alert('注册成功')
              this.$router.push('/Login')
            } else if (this.name === "" || this.password === "" || this.rePassword === "" || this.card === "" || this.relName === "") {
              this.$alert('未填写完整')
              this.initialDate()
            } else if (response.data.code === "false"){
              this.$alert('该账号已存在')
              this.initialDate()
            }
          })
        }
      }
      if (this.identity === "teacher") {
        if (this.password !== this.rePassword) {
          this.$alert('两次密码不一致')
          this.initialDate()
        } else {
          this.$axios.post('teacher/register/', {
            teacherId: this.card,
            teacherName: this.relName,
            teacherEmail: this.name,
            teacherPassword: this.password
          }).then((response) => {
            if (response.data.code === "success") {
              this.$alert('注册成功')
              this.$router.push('/Login')
            } else if (response.data.code === "exist") {
              this.$alert('该账号已存在')
              this.initialDate()
            } else {
              this.$alert('未填写完整')
              this.initialDate()
            }
          })
        }
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
  background-color: #409EFF;
  width: 700px;
  height: 700px;
  margin-right: auto;
  margin-left: auto;
  border-radius: 30px;
  margin-top: 70px;
}
h1 {
  padding-top: 50px;
  font-size: 50px;
  padding-bottom: 10px;
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
.repeat-password {
  width: 700px;
  height: 80px;
  font-size: 20px;
  margin-left: -50px;
  color: #fff;
}
.real-name {
  width: 700px;
  height: 80px;
  font-size: 20px;
  margin-left: -50px;
  color: #fff;
}
.card {
  width: 700px;
  height: 80px;
  font-size: 20px;
  margin-left: -53px;
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
.repeat-in-pass {
  width: 300px;
  height: 30px;
  border-radius: 12px;
}
.in-card {
  width: 300px;
  height: 30px;
  border-radius: 12px;
}
.in-real-name {
  width: 300px;
  height: 30px;
  border-radius: 12px;
}
.box {
  width: 700px;
  height: 80px;
}
.register {
  float: left;
  width: 100px;
  height: 40px;
  font-size: 20px;
  margin-left: 200px;
  background-color: #fff;
  color: #409EFF;
  border-radius: 15px;
}
.back {
  float: right;
  width: 100px;
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
  margin-right: -83px;
  color: #fff;
}
.student {
  float: right;
  margin-right: 260px;
  color: #fff;
}
.teacher {
  float: right;
  margin-right: 55px;
  color: #fff;
}
</style>
