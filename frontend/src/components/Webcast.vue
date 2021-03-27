<template>
  <div class="webcast-container">
    <div class="webcast-window">
      <video-player
        class="video-player vjs-custom-skin"
        ref="videoPlayer"
        :playsinline="true"
        :options="playerOptions"
      ></video-player>
    </div>
    <div>
      <el-button
        round
        type="primary"
        plain
        id="WebcastButton"
        @click="getAddress()"
        :style="{'display':(this.identity === 'teacher' ? 'true' : 'none')}"
      >开启直播</el-button>
      <el-button
        round
        type="primary"
        plain
        id="WebcastButton"
        v-clipboard:copy="rtpmUrl"
        @click="rtpmUrlInfo()"
        :style="{'display':(this.identity === 'teacher' ? 'true' : 'none')}"
      >推流地址</el-button>
      <el-button
        round
        type="primary"
        plain
        id="WebcastButton"
        v-clipboard:copy="rtpmName"
        @click="rtpmNameInfo()"
        :style="{'display':(this.identity === 'teacher' ? 'true' : 'none')}"
      >推流名称</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Webcast",
  component: "Webcast",
  props: {
    lessonId: {
      type: String,
    },
    identity: {
      type: String,
    },
  },
  data() {
    return {
      Time: Math.round(new Date().getTime() / 1000) + 86400,
      key: "039157f13429e58d3e0b357614aafedc",
      rtpmUrl: "",
      rtpmName: "",
      playerOptions: {
        muted: false,
        loop: false,
        language: "zh-CN",
        aspectRatio: "3:2",
        fluid: true,
        sources: [
          {
            type: "rtmp/mp4",
            src: "rtmp://tsdaiyun.com.cn/live/" + this.lessonId,
          },
          {
            type: "application/x-mpegURL",
            src: "http://tsdaiyun.com.cn/live/" + this.lessonId + ".m3u8",
          },
        ],
        techOrder: ["flash", "html5"],
        autoplay: true,
        controls: true,
        poster: "poster.jpg",
        width: document.documentElement.clientWidth,
        notSupportedMessage: "此视频暂无法播放，请稍后再试",
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true,
        },
      },
    };
  },
  methods: {
    getAddress() {
      alert(
        "请在OBS中进行以下设置：\n1.服务设置为自定义\n2.将推流地址粘贴至服务器栏\n3.将推流名称粘贴至串流密钥栏\n4.点击开始推流"
      );
    },
    rtpmUrlInfo() {
      alert("推流地址已复制到粘贴板！");
    },
    rtpmNameInfo() {
      alert("推流名称已复制到粘贴板！");
    },
  },
  mounted: function () {
    (this.rtpmUrl = "rtmp://107716.livepush.myqcloud.com/live/"),
      (this.rtpmName =
        this.lessonId +
        "?txSecret=" +
        this.$md5(this.key + this.lessonId + this.Time.toString(16)) +
        "&txTime=" +
        this.Time.toString(16));
  },
};
</script>
<style scoped>
.webcast-container {
  height: 250px;
  width: 300px;
  background-color: #ffffff;
  margin: 0 3px;
  border: solid 1px rgb(195, 195, 195);
  border-radius: 10px 10px 0 0;
  overflow: hidden;
}
.webcast-window {
  height: 220px;
  width: 300px;
  background-color: #000;
}
#WebcastButton {
  padding: 5px;
  margin: 2px 10px;
}
</style>
