import { mount as nativeMount, createLocalVue } from '@vue/test-utils';
import Vuetify from 'vuetify';
import Vuex from 'vuex';

const storeObject = {
  modules: {
    hacknight: {
      namespaced: true,
      getters: {
        getHacknights: jest.fn(() => []),
        getHacknight: jest.fn(() => ({ participants: [] })),
        getError: jest.fn()
      },
      actions: { getHacknights: jest.fn() }
    },
    participant: {
      namespaced: true,
      getters: { getParticipants: jest.fn(() => []), getError: jest.fn() },
      actions: { getParticipants: jest.fn() }
    },
    auth: {
      namespaced: true,
      getters: { getError: jest.fn() }
    },
    contact: {
      namespaced: true,
      getters: { successfullySent: jest.fn(), msgErrorRaised: jest.fn() }
    }
  }
};

// mount function from @vue/test-utils
// needs this enhancement to render vuetify components correctly
// source: https://vuetifyjs.com/en/getting-started/unit-testing/#mocking-vuetify

export const getMountWithVuetify = () => {
  const localVue = createLocalVue();
  const vuetify = new Vuetify();

  return Component => {
    return nativeMount(Component, { localVue, vuetify });
  };
};

// mount function from @vue/test-utils
// needs this enhancement to render components using vuex correctly
// source: https://vue-test-utils.vuejs.org/guides/using-with-vuex.html

export const getMountWithVuex = () => {
  const localVue = createLocalVue();
  localVue.use(Vuex);

  return Component => {
    const store = new Vuex.Store(storeObject);

    return nativeMount(Component, { store, localVue, stubs: ['apexchart'] });
  };
};

// Use this function if you need to test a component
// that uses both Vuex and Vuetify

export const getMountWithProviders = () => {
  const localVue = createLocalVue();
  localVue.use(Vuex);
  const vuetify = new Vuetify();

  return Component => {
    const store = new Vuex.Store(storeObject);

    return nativeMount(Component, {
      store,
      localVue,
      vuetify,
      stubs: ['apexchart']
    });
  };
};
