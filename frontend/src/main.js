import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VideoPlayer from 'vue-video-player';
import VueSocketIO from 'vue-socket.io';
import 'videojs-flash';
import 'videojs-contrib-hls';
import md5 from 'js-md5';
Vue.prototype.$md5 = md5
import VueClipboard from 'vue-clipboard2'
VueClipboard.config.autoSetContainer = true
Vue.use(VueClipboard)
require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')
Vue.use(VideoPlayer)

Vue.use(new VueSocketIO({
  debug:true,
  connection:'http://localhost:8080',
}))
axios.defaults.withCredentials = true
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

Vue.prototype.$axios = axios.create({
  baseURL: process.env.VUE_APP_API_BASE,
  timeout: 3000
})
Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
