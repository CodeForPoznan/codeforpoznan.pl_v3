import { createRouter, createWebHashHistory } from 'vue-router';
import HomePage from './components/HomePage/HomePage.vue';
import LoginForm from './components/Login/LoginForm.vue';
import DashboardMain from './components/Dashboard/DashboardMain.vue';
import store from './store';

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: LoginForm },
  {
    path: '/dashboard',
    component: DashboardMain,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/isLoggedIn']) {
        next('/login');
      } else {
        next();
      }
    },
  },
  { path: '/:notFound(.*)', redirect: '/' },
];

export default createRouter({
  history: createWebHashHistory(),
  routes,
});
