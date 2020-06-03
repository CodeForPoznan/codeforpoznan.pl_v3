import Vue from 'vue';
import VueRouter from 'vue-router';

import HomePage from './components/HomePage.vue';
import Login from './components/Login.vue';
import Dashboard from './components/Dashboard.vue';
import store from './store';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: Login },
  {
    path: '/dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/isLoggedIn']) {
        next('/login');
      } else {
        next();
      }
    }
  }
];

export default new VueRouter({ mode: 'history', routes });
