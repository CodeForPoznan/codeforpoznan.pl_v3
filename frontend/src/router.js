import Vue from 'vue';
import VueRouter from 'vue-router';

import HomePage from './components/HomePage.vue';
import Login from './components/Login.vue';

Vue.use(VueRouter);

const routes = [
    { path: '/', component: HomePage },
    { path: '/login', component: Login }
];

export default new VueRouter({ mode: 'history', routes });
