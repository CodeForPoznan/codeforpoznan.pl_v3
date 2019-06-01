import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth';
import contact from './modules/contact';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {},
    getters: {},
    mutations: {},
    actions: {},

    modules: {
        auth,
        contact
    }
});

export default store;
