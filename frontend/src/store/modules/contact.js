import axios from 'axios';

export default {
  namespaced: true,
  state: {
    msgWasSent: null,
    msgError: null
  },
  getters: {
    successfullySent: state => {
      return state.msgWasSent;
    },
    msgErrorRaised: state => {
      return state.msgError;
    }
  },
  mutations: {
    setWasSent(state) {
      state.msgWasSent = true;
      setTimeout(() => (state.msgWasSent = false), 5000);
    },
    setWasntSent(state) {
      state.msgWasSent = false;
    },
    raiseMsgError(state) {
      state.msgError = true;
      setTimeout(() => (state.msgError = false), 5000);
    },
    clearError(state) {
      state.msgError = false;
    }
  },
  actions: {
    sentMessage({ commit }, contactForm) {
      return new Promise((resolve, reject) => {
        axios
          .post('/api/send-email/', {
            name: contactForm.name,
            email: contactForm.email,
            phone: contactForm.phone,
            content: contactForm.content
          })
          .then(
            response => {
              if (response.status == 200) commit('setWasSent');
              resolve(response);
            },
            error => {
              reject(error);
            }
          );
      });
    },
    setingWasntSent({ commit }) {
      commit('setWasntSent');
    },
    setingClearError({ commit }) {
      commit('clearError');
    }
  }
};
