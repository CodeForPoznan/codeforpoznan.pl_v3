import axios from 'axios';

export default {
  namespaced: true,
  state: {
    allHacknights: [],
    hacknight: null,
    error: null
  },
  getters: {
    getHacknights(state) {
      return state.allHacknights;
    },
    getHacknight(state) {
      return state.hacknight;
    },
    getError(state) {
      return state.error;
    }
  },
  mutations: {
    raiseError(state, error_msg) {
      state.error = error_msg;
    },
    setHacknights(state, hacknights) {
      state.allHacknights = hacknights;
    },
    setHacknight(state, hacknight) {
      state.hacknight = hacknight;
    }
  },
  actions: {
    createHacknight({ commit, dispatch }) {
      return axios
        .post('/hacknights/', {
          date: new Date().toISOString().slice(0, 10)
        })
        .then(res => {
          commit('setHacknight', res.data);
          dispatch('getHacknights');
        })
        .catch(error => {
          const err_msg = error.response.data.message;

          commit('raiseError', err_msg);
        });
    },
    getHacknight({ commit }, hacknight_id) {
      axios
        .get(`/hacknights/${hacknight_id}/`)
        .then(res => {
          commit('setHacknight', res.data.hacknights);
        })
        .catch(error => {
          commit('raiseError', error);
        });
    },
    getHacknights({ commit }) {
      axios
        .get('/hacknights/')
        .then(res => {
          commit('setHacknights', res.data);
        })
        .catch(error => {
          commit('raiseError', error);
        });
    },
    addParticipants({ commit, getters }, participants_ids) {
      axios
        .post(`/hacknights/${getters.getHacknight.id}/participants/`, {
          participants_ids: participants_ids
        })
        .then(res => {
          commit('setHacknight', res.data);
        })
        .catch(error => {
          commit('raiseError', error);
        });
    }
  }
};
