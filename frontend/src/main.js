import Vue from 'vue';
import Vuelidate from 'vuelidate';
import 'vuetify/dist/vuetify.min.css';

import axios from 'axios';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import App from './App.vue';

Vue.use(Vuelidate);

Vue.config.productionTip = false;
axios.defaults.baseURL = 'http://0.0.0.0:5000/';

const token = localStorage.getItem('token');

if (token) {
  axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
}

export const interceptorRefresh = axios.interceptors.response.use(
  response => response,
  error => {
    if (
      error.response.status === 401 &&
      error.response.data.msg.includes('expired') &&
      !error.config.url.includes('refresh')
    ) {
      store
        .dispatch('auth/refresh')
        .then(() => {
          delete error.config.headers['Authorization'];
          return axios.request(error.config);
        })
        .catch(() => {
          axios.interceptors.response.eject(interceptorRefresh);
          localStorage.removeItem('token');
          localStorage.removeItem('refresh_token');
          router.push('/login');
        });
    } else {
      return Promise.reject(error);
    }
  }
);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app');
