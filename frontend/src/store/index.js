import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth';
import contact from './modules/contact';
import hacknight from './modules/hacknight';
import participant from './modules/participant';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},

  modules: {
    auth,
    contact,
    hacknight,
    participant
  }
});

export default store;
