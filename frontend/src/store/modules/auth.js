import axios from 'axios';

import { interceptorRefresh } from '../../main.js';
import router from '../../router.js';

export default {
  namespaced: true,
  state: {
    token: localStorage.getItem('token') || '',
    error: null
  },
  getters: {
    isLoggedIn: state => !!state.token,
    getError(state) {
      return state.error;
    }
  },
  mutations: {
    raiseError(state, error_msg) {
      state.error = error_msg;
    },
    setToken(state, token) {
      state.token = token;
    }
  },
  actions: {
    async login({ commit }, loginData) {
      delete axios.defaults.headers.common['Authorization'];

      try {
        let res = await axios.post('/api/auth/login/', {
          username: loginData.username,
          password: loginData.password
        });
        const token = res.data.access_token;
        const refresh_token = res.data.refresh_token;

        localStorage.setItem('token', token);
        localStorage.setItem('refresh_token', refresh_token);
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
        commit('setToken', token);
        router.push('/dashboard');
        return res.status;
      } catch (error) {
        localStorage.removeItem('token');
        commit('raiseError', error);
      }
    },
    logout({ dispatch }) {
      axios.interceptors.response.eject(interceptorRefresh);
      return axios
        .delete('/api/auth/logout/')
        .then(() => {
          localStorage.removeItem('token');
        })
        .catch(() => {
          localStorage.removeItem('token');
        })
        .finally(() => {
          delete axios.defaults.headers.common['Authorization'];
          dispatch('revoke');
        });
    },
    revoke() {
      const refresh_token = localStorage.getItem('refresh_token');

      return axios
        .delete('/api/auth/refresh-token/', {
          headers: { Authorization: 'Bearer ' + refresh_token }
        })
        .then(() => {
          localStorage.removeItem('refresh_token');
        })
        .catch(() => {
          localStorage.removeItem('refresh_token');
        });
    },
    refresh() {
      const refresh_token = localStorage.getItem('refresh_token');

      return axios
        .post('/api/auth/refresh/', null, {
          headers: {
            Authorization: 'Bearer ' + refresh_token
          }
        })
        .then(res => {
          const token = res.data.access_token;

          localStorage.setItem('token', token);
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
          return res;
        })
        .catch(error => {
          localStorage.removeItem('token');
          localStorage.removeItem('refresh_token');
          throw error;
        });
    }
  }
};
