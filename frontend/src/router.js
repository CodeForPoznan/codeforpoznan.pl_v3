import Vue from 'vue'
import VueRouter from 'vue-router'

import HomePage from './components/HomePage.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: HomePage }
]

export default new VueRouter({mode: 'history', routes})
