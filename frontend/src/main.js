import { createApp } from 'vue';
import VueApexCharts from 'vue3-apexcharts';
import VueGtag from 'vue-gtag';
import 'vuetify/dist/vuetify.min.css';

import axios from 'axios';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import App from './App.vue';

axios.defaults.baseURL = process.env.VUE_APP_AXIOS_BASE_URL || '/';
const token = localStorage.getItem('token');

if (token) {
  axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
}

export const interceptorRefresh = axios.interceptors.response.use(
  (response) => response,
  (error) => {
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

const app = createApp(App);

app.use(VueApexCharts);
app.use(vuetify);
app.use(router);
app.use(store);
app.use(
  VueGtag,
  {
    config: {
      id: 'UA-88692971-1',
      enabled: process.env.NODE_ENV === 'production',
      params: {
        anonymize_ip: true,
      },
    },
  },
  router
);
app.mount('#app');
