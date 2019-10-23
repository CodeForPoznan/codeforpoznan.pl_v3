import Vue from 'vue';
import VueRouter from 'vue-router';

import HomePage from './components/HomePage.vue';
import Login from './components/Login.vue';
import Dashboard from './components/Dashboard.vue';

Vue.use(VueRouter);

const routes = [
    { path: '/', component: HomePage },
    { path: '/login', component: Login },
    { path: '/dashboard', component: Dashboard}
];

export default new VueRouter({ mode: 'history', routes });
