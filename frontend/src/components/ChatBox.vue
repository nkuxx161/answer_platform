<template>
  <div>
    <div class="chat-box-container">
      <div class="chat-box-content">
        <ul class="chat-box-ul">
          <li v-for="item in chatList" :key="item.name" class="chat-box-li">
            <div class="chat-information" v-show="item.personId !== personId">
              <el-avatar class="chat-icon" :size="35" shape="square" :src="circleUrl"></el-avatar>
              <span class="chat-name">{{item.chatName}}：</span>
            </div>
            <div class="my-information" v-show="item.personId === personId">
              <span class="my-name">我</span>
            </div>
            <div class="chat-frame" v-show="item.personId !== personId">
              <span class="chat-content">
                {{item.chatContent}}
              </span>
            </div>
            <div class="my-chat-frame" v-show="item.personId === personId">
              <span class="my-chat-content">
                {{item.chatContent}}
              </span>
            </div>
          </li>
        </ul>
      </div>
      <el-form :inline="true" class="[demo-form-inline,chat-box-form]">
        <el-input
          type="textarea"
          :autosize="{ minRows: 2, maxRows: 2}"
          placeholder="请输入内容"
          v-model="comment"
          class="chat-box-text"
        ></el-input>
        <el-button type="primary" class="chat-box-submit" @click="submitComment()">发送</el-button>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChatBox",
  props: {
    studentName: {
      type: String,
    },
    lessonId: {
      type: String,
    },
    personId: {
      type: String,
    }
  },
  data() {
    return {
      circleUrl:
        "https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png",
      intervalId: "",
      chatList: [],
      comment: "",
    };
  },
  mounted() {
    this.intervalId = setInterval(() => {
      this.getChatNote();
    }, 100);
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
  },
  methods: {
    getChatNote() {
      this.$axios
        .post("chatting/checkNote/", { lessonId: this.lessonId })
        .then((response) => {
          this.chatList = response.data.recordList;
        });
    },

    submitComment() {
      if (this.comment !== "") {
        this.$axios
          .post("chatting/makeNote/", {
            lessonId: this.lessonId,
            chatName: this.studentName,
            chatContent: this.comment,
            personId: this.personId,
          })
          .then(() => {
            this.comment = "";
          });
      } else alert("不能发送空消息");
    },
  },
  component: "ChatBox",
};
</script>

<style scoped>
.chat-box-container {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  height: 820px;
  width: 350px;
  border: solid 1px rgb(195, 195, 195);
  border-radius: 10px;
  margin: 0 5.5px;
  background-color: rgb(248, 248, 248);
}
.chat-box-content {
  height: 730px;
  overflow-y: auto;
}
.chat-box-ul {
  list-style: none;
  padding: 0;
}
.chat-box-li {
  padding: 5px;
  margin: 1px;
}
.chat-box-form {
  width: 30px;
  height: 500px;
  background-color: red;
}
.chat-box-text {
  width: 80%;
  resize: none;
  vertical-align: middle;
  width: 210px;
  margin: 10px;
}
.chat-box-submit {
  margin: 10.5px 0;
  vertical-align: middle;
  height: 52px;
}
.chat-information {
  height: 40px;
}
.my-information {
  height: 30px;
}
.chat-name {
  display: block;
  margin: 5px 0px 10px 45px;
  letter-spacing: 0px;
  line-height: 32px;
  font-size: 13px;
  width: 200px;
  word-break: break-all;
  white-space: pre-wrap;
  text-align: left;
}
.my-name {
  display: block;
  float: right;
  line-height: 32px;
  font-size: 13px;
  word-break: break-all;
  white-space: pre-wrap;
  text-align: left;
}
.chat-frame {
  width: auto;
  text-align: left;
}
.my-chat-frame {
  width: auto;
  text-align: right;
}
.chat-content {
  border: solid 0px;
  border-radius: 10px;
  padding: 5px 10px 5px 10px;
  background-color: rgba(64, 224, 208, 0.7);
  display: inline-block;
  letter-spacing: 1px;
  line-height: 20px;
  font-size: 13px;
  width: auto;
  word-break: break-all;
  white-space: pre-wrap;
  text-align: left;
}
.my-chat-content {
  border: solid 0px;
  border-radius: 10px;
  padding: 5px 10px 5px 10px;
  background-color: #40a0ffc0;
  display: inline-block;
  letter-spacing: 1px;
  line-height: 20px;
  font-size: 13px;
  width: auto;
  word-break: break-all;
  white-space: pre-wrap;
  text-align: left;
}
.chat-icon {
  float: left;
}

</style>
