import '@mdi/font/css/materialdesignicons.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '../assets/icons.js';
import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import Icons from '../assets/icons.js';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'fa',
    values: Icons
  }
});
