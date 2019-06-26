import axios from 'axios';
axios.defaults.baseURL = 'http://0.0.0.0:5000/';

export default {
    namespaced: true,
    state: {
        token: localStorage.getItem('token') || ''
    },
    getters: {
        isLoggedIn: state => !!state.token
    },
    mutations: {
        auth_success(state, token) {
            state.token = token;
        }
    },
    actions: {
        login({ commit }, loginData) {
            return new Promise((resolve, reject) => {
                axios
                    .post('auth/login', {
                        username: loginData.username,
                        password: loginData.password
                    })
                    .then(
                        res => {
                            const token = res.data.access_token;

                            localStorage.setItem('token', token);
                            axios.defaults.headers.common['Authorization'] =
                                'Bearer ' + token;
                            commit('auth_success', token);
                            resolve(res);
                        },
                        error => {
                            localStorage.removeItem('token');
                            reject(error);
                        }
                    );
            });
        }
    }
};
