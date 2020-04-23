import axios from 'axios';

export default {
  namespaced: true,
  state: {
    allParticipants: [],
    error: null
  },
  getters: {
    getParticipants(state) {
      return state.allParticipants;
    },
    getError(state) {
      return state.error;
    }
  },
  mutations: {
    raiseError(state, error_msg) {
      state.error = error_msg;
    },
    setParticipants(state, participants) {
      state.allParticipants = participants;
    }
  },
  actions: {
    getParticipants({ commit }) {
      axios
        .get('/participants/')
        .then(res => {
          commit('setParticipants', res.data);
        })
        .catch(error => {
          commit('raiseError', error);
        });
    }
  }
};
