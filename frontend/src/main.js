import Vue from 'vue';
import App from './App.vue';
import Vuelidate from 'vuelidate';
import 'vuetify/dist/vuetify.min.css';

import axios from 'axios';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';

Vue.use(Vuelidate);

Vue.config.productionTip = false;
axios.defaults.baseURL = 'http://0.0.0.0:5000/';

const token = localStorage.getItem('token');

if (token) {
  axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
}

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app');
