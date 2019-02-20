
import Vue from 'vue';
import Vuex from 'vuex';
import contact from './modules/contact'

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions : {},

  modules: {
    contact
  }
})

export default store;
