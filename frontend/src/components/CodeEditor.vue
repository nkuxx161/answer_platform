<template>
  <div id="editor" @keyup="sendContentMessage()">
    <el-header class="header" height="52px">
      <div class="lang">
        语言:
        <el-select class="lan-select" placeholder="javascript" size="small" v-model="lang">
          <el-option value="javascript">javascript</el-option>
          <el-option value="css">css</el-option>
          <el-option value="python">python</el-option>
          <el-option value="c_cpp">c_c++</el-option>
          <el-option value="java">java</el-option>
          <el-option value="r">r</el-option>
          <el-option value="matlab">matlab</el-option>
        </el-select>
      </div>
      <div class="theme">
        主题:
        <el-select class="theme-select" placeholder="ambiance" size="small" v-model="theme">
          <el-option-group label="dark">
            <el-option value="ambiance">ambiance</el-option>
            <el-option value="chaos">chaos</el-option>
            <el-option value="cobalt">cobalt</el-option>
            <el-option value="dracula">dracula</el-option>
          </el-option-group>
          <el-option-group label="bright">
            <el-option value="chrome">chrome</el-option>
            <el-option value="clouds">clouds</el-option>
            <el-option value="dawn">dawn</el-option>
            <el-option value="dreamweaver">dreamweaver</el-option>
          </el-option-group>
        </el-select>
      </div>
    </el-header>
    <editor
      v-model="content"
      @init="initEditor()"
      height="768px"
      width="1250px"
      border-radius="10px"
      :lang="lang"
      :theme="theme"
    ></editor>
  </div>
</template>

<script>
export default {
  name: "vueEditor",
  components: {
    editor: require("vue2-ace-editor"),
  },
  props: {
    lessonId: {
      type: String,
    },
    lessonName: {
      type: String,
    },
  },
  sockets: {},
  data() {
    return {
      content: "",
      theme: "ambiance",
      lang: "javascript",
    };
  },
  mounted() {
    this.sockets.listener.subscribe("getContent", (data) => {
      this.content = data;
    });
    this.$axios
      .post("lesson/getCode/", { lessonId: this.lessonId })
      .then((response) => {
        this.content = response.data.codeContent;
      });
  },
  methods: {
    initEditor() {
      require("brace/ext/language_tools");
      require("brace/mode/yaml");
      require("brace/mode/javascript");
      require("brace/mode/python");
      require("brace/mode/html");
      require("brace/mode/r");
      require("brace/mode/java");
      require("brace/mode/matlab");
      require("brace/mode/css");
      require("brace/mode/c_cpp");
      require("brace/mode/less");
      require("brace/theme/ambiance");
      require("brace/theme/chrome");
      require("brace/theme/chaos");
      require("brace/theme/clouds");
      require("brace/theme/cobalt");
      require("brace/theme/dawn");
      require("brace/theme/dracula");
      require("brace/theme/dreamweaver");
    },
    themeChange(event) {
      this.theme = event.currentTarget.Themevalue;
    },
    langChange(event) {
      this.lang = event.currentTarget.Langvalue;
    },
    sendContentMessage: function () {
      this.$socket.emit("changeContent", this.content);
      this.$axios.post("lesson/updateCode/", {
        lessonId: this.lessonId,
        codeContent: this.content,
      });
    },
  },
};
</script>

<style scoped>
#editor {
  position: relative;
  height: 820px;
  width: 1250px;
  background-color: #f2e6e6;
  border-radius: 10px;
  margin: 10px 0;
  border: solid 1px rgb(195, 195, 195);
  overflow: hidden;
}
.head {
  position: absolute;
  left: 370px;
  line-height: 50px;
  font-size: 16px;
}
.lang {
  position: absolute;
  display: inline-block;
  right: 20px;
  margin: 10px 10px 0 0;
}
.theme {
  position: absolute;
  display: inline-block;
  right: 290px;
  margin: 10px 10px 0 0;
}
.header {
  background-color: #c0c4cc;
}
</style>
