import Vue from 'vue'
import VueRouter from 'vue-router'
import Backstage from '../views/Backstage.vue'
import Room from '../views/Room.vue'
import LessonList from '../views/LessonList.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/Backstage',
    name: 'Backstage',
    component: Backstage
  },
  {
    path: '/Room',
    name: 'Room',
    component: Room
  },
  {
    path: '/LessonList',
    name: 'LessonList',
    component: LessonList
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  }
]

const router = new VueRouter({
  routes
})

export default router
