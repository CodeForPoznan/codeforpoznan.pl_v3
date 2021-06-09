import axios from 'axios';

export default {
  namespaced: true,
  state: {
    allParticipants: [],
    error: null,
    Participant: null
  },
  getters: {
    getParticipants(state) {
      return state.allParticipants;
    },
    getError(state) {
      return state.error;
    },
    getParticipant(state) {
      return state.Participant;
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
      state.Participant = participant;
    }
  },
  actions: {
    getParticipants({ commit }) {
      axios
        .get('/api/participants/')
        .then(res => {
          commit('setParticipants', res.data);
        })
        .catch(error => {
          commit('raiseError', error);
        });
    },
    createParticipant({ commit, dispatch }, newParticipantData) {
      return axios
        .post('/api/participants/', { ...newParticipantData })
        .then(res => {
          commit('setParticipant', res.data);
          dispatch('getParticipants');
          return res.status;
        })
        .catch(error => {
          commit('raiseError', error);
        });
    },
    async getParticipant({ commit }, participantId) {
      try {
        const res = await axios.get(`/api/participants/${participantId}/`);

        commit('setParticipant', res.data);
      } catch (error) {
        commit('raiseError', error);
      }
    },
    async editParticipant({ commit, dispatch, getters }, participantNewData) {
      try {
        const res = await axios.put(
          `/api/participants/${getters.getParticipant.id}/`,
          { ...participantNewData }
        );

        commit('setParticipant', res.data);
        dispatch('getParticipants');
        return res.status;
      } catch (error) {
        commit('raiseError', error);
      }
    }
  }
};
