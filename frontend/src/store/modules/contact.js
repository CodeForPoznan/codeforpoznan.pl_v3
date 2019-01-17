import axios from 'axios';
axios.defaults.baseURL = 'http://0.0.0.0:5000/'

export default {
  namespaced: true,
  state: {
    msgWasSent: null
  },
  getters: {
    successfullySent: state => {
      return state.msgWasSent;
    }
  },
  mutations: {
    setWasSent (state) {
      state.msgWasSent = true
    },
    setWasntSent (state) {
      state.msgWasSent = false
    }
  },
  actions: {
    sentMessage ({commit}, contactForm) {
      axios.post('send-email/', {
        name: contactForm.name,
        email: contactForm.email,
        phone: contactForm.phone,
        content: contactForm.content
      })
      .then(response => {
        if (response.status == 201) commit('setWasSent')
      })
      .catch(error => {
        console.log(error)
      })
    },
    setingWasntSent ({commit}) {
      commit('setWasntSent')
    }
  }
}
