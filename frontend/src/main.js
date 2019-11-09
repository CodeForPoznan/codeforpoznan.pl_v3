import Vue from 'vue';
import App from './App.vue';
import Vuelidate from 'vuelidate';
import Vuetify from 'vuetify/lib';
import 'vuetify/dist/vuetify.min.css';

import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';

Vue.use(Vuelidate);
Vue.use(Vuetify);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app');
