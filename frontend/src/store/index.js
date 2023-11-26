import { createStore } from 'vuex';
import auth from './modules/auth';
import contact from './modules/contact';
import hacknight from './modules/hacknight';
import participant from './modules/participant';

const store = createStore({
  state: {},
  getters: {},
  mutations: {},
  actions: {},

  modules: {
    auth,
    contact,
    hacknight,
    participant,
  },
});

export default store;
