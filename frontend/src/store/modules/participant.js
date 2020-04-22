import axios from 'axios';

export default {
  namespaced: true,
  state: {
    allParticipants: [],
    error: null,
    newParticipant: null
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
    },
    setParticipant(state, participant) {
      state.newParticipant = participant;
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
    },
    createParticipant({ commit, dispatch }, newParticipantData) {
      return axios
        .post('/participants/', {
          first_name: newParticipantData.first_name,
          last_name: newParticipantData.last_name,
          email: newParticipantData.email,
          github: newParticipantData.github,
          phone: newParticipantData.phone,
          slack: newParticipantData.slack
        })
        .then(res => {
          commit('setParticipant', res.data);
          dispatch('getParticipant');
        });
    }
  }
};
