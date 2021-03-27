<template>
  <div class="home">
    <h1>在线答疑平台</h1>
    <div class="box">
      <router-link to="/Login">
        <el-button round class="login">
        登录
        </el-button>
      </router-link>
      <router-link to="/Register">
        <el-button round class="register">
        注册
        </el-button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>

<style scoped>
body {
  margin: 0;
}
h1 {
  padding-top: 80px;
  font-size: 50px;
  padding-left: 200px;
  padding-right: 200px;
  margin-left: 0;
  color: #fff;
}
.home {
  background-color: #409EFF;
  border-radius: 30px;
  width: 700px;
  height: 400px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 150px;
}
.box {
  height: 200px;
  width: 700px;
}
.login {
  font-size: 20px;
  width: 100px;
  height: 70px;
  margin-top: 60px;
  margin-left: 120px;
  float: left;
  background-color: #fff;
  color: #409EFF;
}
.register {
  font-size: 20px;
  width: 100px;
  height: 70px;
  margin-top: 60px;
  margin-right: 120px;
  float: right;
  background-color: #fff;
  color: #409EFF;
}
</style>
