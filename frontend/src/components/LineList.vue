<template>
  <div>
    <div class="line-list-container">
      <p class="line-list-head">排队列表</p>
      <div class="line-list-content" style="overflow:auto">
        <ol class="line-list-ol">
          <li v-for="(item, i) in lineList" :key="item.id" class="line-list-li">
            <div class="line-list-num">
              <span>{{i+1}}</span>
            </div>
            <div class="line-list-order">
              <span>{{item.studentName}}</span>
            </div>
            <div class="line-list-id">
              <span>{{item.studentId}}</span>
            </div>
          </li>
        </ol>
      </div>
      <div>
        <el-button
          type="primary"
          plain
          value="排队"
          id="LineListButton"
          @click="inLine()"
          :style="{'display':(this.identity === 'student' ? 'true' : 'none')}"
        >排队</el-button>
        <el-button
          type="primary"
          plain
          value="退出"
          id="LineListButton"
          @click="outLine()"
          :style="{'display':(this.identity === 'student' ? 'true' : 'none')}"
        >退出</el-button>
        <el-button
          type="primary"
          plain
          value="退出"
          id="LineListTeaherButton"
          @click="outLine()"
          :style="{'display':(this.identity === 'teacher' ? 'true' : 'none')}"
        >移出首位学生</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LineList",
  props: {
    studentName: {
      type: String,
    },
    studentId: {
      type: String,
    },
    lessonId: {
      type: String,
    },
    identity: {
      type: String,
    },
  },
  data() {
    return {
      intervalId: "",
      lineList: [],
    };
  },
  components: "LineList",
  methods: {
    inLine() {
      if (this.identity === "student") {
        this.$axios
          .post("waitLine/joinLine/", {
            lessonId: this.lessonId,
            studentId: this.studentId,
            studentName: this.studentName,
          })
          .then((response) => {
            if (response.data.code === "false") alert("你已在队列中！");
          });
      }
    },
    outLine() {
      if (this.identity === "student") {
        let index = null;
        if (this.lineList === undefined) {
          index = -1;
        } else {
          index = this.lineList.findIndex((item) => {
            return item.studentId === this.studentId;
          });
        }
        if (index !== -1) {
          this.$axios.post("waitLine/quitLine/", {
            lessonId: this.lessonId,
            id: this.lineList[index].id,
          });
        } else alert("你不在队列中！");
      }
      if (this.identity === "teacher") {
        this.$axios.post("waitLine/quitLine/", {
          lessonId: this.lessonId,
          id: this.lineList[0].id,
        });
      }
    },
    getLineList() {
      this.$axios
        .post("waitLine/getLine/", { lessonId: this.lessonId })
        .then((response) => {
          this.lineList = response.data.lineList;
        });
    },
  },
  mounted() {
    this.intervalId = setInterval(() => {
      this.getLineList();
    }, 100);
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
  },
};
</script>

<style scoped>
.line-list-container {
  border: 1px solid #785;
  font-size: 10px;
  height: 568px;
  width: 300px;
  border: solid 1px rgb(195, 195, 195);
  border-radius: 0 0 10px 10px;
  overflow: hidden;
  margin: 0 3px;
}
.line-list-head {
  margin: 0 0 3px 0;
  border-bottom: solid 1px rgb(195, 195, 195);
  font-size: 20px;
  font-family: "宋体";
  height: 35px;
}
.line-list-content {
  margin: 0;
  height: 480px;
}
.line-list-ol {
  padding: 0px;
  margin: 0;
}
.line-list-li {
  padding: 5px 0 5px 0;
  margin: 1px;
  height: 24px;
  font-size: 12px;
  color: rgb(121, 127, 137);
  font-family: -apple-system, Microsoft Yahei, sans-serif;
  background-color: #ffffff;
  text-align: left;
}
.line-list-num {
  display: inline-block;
  background-color: rgb(238, 238, 238);
  color: rgb(153, 153, 153);
  height: 20px;
  width: 20px;
  border: solid;
  border-width: 0;
  border-radius: 50%;
  text-align: center;
  margin: 0 30px 0 30px;
  line-height: 20px;
}
.line-list-order {
  display: inline-block;
  line-height: 20px;
  width: 60px;
}
.line-list-id {
  display: inline-block;
  line-height: 20px;
  margin: 0 0 0 30px;
}
#LineListButton {
  height: 35px;
  width: 55px;
  font-size: 15px;
  margin: 10px 20px;
  padding: 5px;
}
#LineListTeacherButton {
  height: 35px;
  width: 100px;
}
</style>
