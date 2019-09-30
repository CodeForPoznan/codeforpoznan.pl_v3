import axios from 'axios';

export default {
    namespaced: true,
    state: {

    },
    getters: {

    },
    mutations: {

    },
    actions: {
      createHacknight({commit}) {
        return new Promise ((resolve, reject) => {
          const d = new Date();
          axios.post('/hacknights/', {
            date: d.toUTCString()
          })
          .then(res => {
            resolve(res);
          }, error => {
            reject(error);
          })
        })
      },
      getHacknight({commit}, hacknight_id) {
        return new Promise ((resolve, reject) => {
          axios.get(`/hacknights/${hacknight_id}/`)
          .then(res => {
            resolve(res);
          }, error => {
            reject(error);
          })
        })
      },
      getHacknights({commit}) {
        return new Promise ((resolve, reject) => {
          axios.get('/hacknights/')
          .then(res => {
            resolve(res);
          }, error => {
            reject(error);
          })
        })
      },
      getParticipants({commit}) {
        return new Promise ((resolve, reject) => {
          axios.get('/participants/')
          .then(res => {
            resolve(res);
          }, error => {
            reject(error);
          })
        })
      },
      addParticipants({commit}, data) {
        return new Promise ((resolve, reject) => {
          axios.patch(`/hacknights/${data.hacknight_id}/`, {
            participants: data.participants_ids
          })
          .then(res => {
            resolve(res);
          }, error => {
            reject(error);
          })
        })
      }
    }
};
