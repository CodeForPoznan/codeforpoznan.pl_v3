import Vue from 'vue'
import VueRouter from 'vue-router'

import HomePage from './components/HomePage'
import Login from './components/Login'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: Login }
]

export default new VueRouter({mode: 'history', routes})
