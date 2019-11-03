import axios from 'axios';

export default {
  namespaced: true,
  state: {
    success: null,
    error: null
  },
  getters: {},
  mutations: {
    wasSuccess(state) {
      state.success = true;
    },
    raiseError(state) {
      state.error = true;
    }
  },
  actions: {
    createHacknight({ commit }) {
      return new Promise((resolve, reject) => {
        const d = new Date();

        axios
          .post('/hacknights/', {
            date: d.toUTCString()
          })
          .then(
            res => {
              commit('wasSuccess');
              resolve(res);
            },
            error => {
              commit('raiseError');
              reject(error);
            }
          );
      });
    },
    getHacknight({ commit }, hacknight_id) {
      return new Promise((resolve, reject) => {
        axios.get(`/hacknights/${hacknight_id}/`).then(
          res => {
            commit('wasSuccess');
            resolve(res);
          },
          error => {
            reject(error);
          }
        );
      });
    },
    getHacknights({ commit }) {
      return new Promise((resolve, reject) => {
        axios.get('/hacknights/').then(
          res => {
            commit('wasSuccess');
            resolve(res);
          },
          error => {
            commit('raiseError');
            reject(error);
          }
        );
      });
    }
  }
};
