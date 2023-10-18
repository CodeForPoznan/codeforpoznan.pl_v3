import { mount as nativeMount } from '@vue/test-utils';
import { vi } from 'vitest';
import { createVuetify } from 'vuetify';
import { createStore } from 'vuex';
import Vuex from 'vuex';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import HacknightWrapper from '../src/components/Dashboard/Hacknight/HacknightWrapper.vue';
import HacknightsParticipants from '../src/components/Dashboard/HacknightsParticipants/HacknightsParticipants.vue';
import DashboardHeader from '../src/components/Dashboard/Header/DashboardHeader.vue';
import ParticipantsSearch from '../src/components/Dashboard/Participants/ParticipantsSearch/ParticipantsSearch.vue';
import ParticipantsList from '../src/components/Dashboard/Participants/ParticipantsList.vue';
import ParticipantsChart from '../src/components/Dashboard/ParticipantsChart/ParticipantsChart.vue';
import DashboardMain from '../src/components/Dashboard/DashboardMain.vue';
import AboutUs from '../src/components/HomePage/AboutUs/AboutUs.vue';
import ContactUs from '../src/components/HomePage/ContactUs/ContactUs.vue';
import HomePageHeader from '../src/components/HomePage/Header/HomePageHeader.vue';
import JoinUs from '../src/components/HomePage/JoinUs/JoinUs.vue';
import OurProjects from '../src/components/HomePage/OurProjects/OurProjects.vue';
import ModalContent from '../src/components/HomePage/OurProjects/ModalContent/ModalContent.vue';
import PageFooter from '../src/components/HomePage/PageFooter/PageFooter.vue';
import SocialMedia from '../src/components/HomePage/SocialMedia/SocialMedia.vue';
import HomePage from '../src/components/HomePage/HomePage.vue';
import LoginForm from '../src/components/Login/LoginForm.vue';

const storeObject = {
  modules: {
    hacknight: {
      namespaced: true,
      getters: {
        getHacknights: vi.fn(() => []),
        getHacknight: vi.fn(() => ({ participants: [] })),
        getError: vi.fn(),
      },
      actions: { getHacknights: vi.fn() },
    },
    participant: {
      namespaced: true,
      getters: { getParticipants: vi.fn(() => []), getError: vi.fn() },
      actions: { getParticipants: vi.fn() },
    },
    auth: {
      namespaced: true,
      getters: { getError: vi.fn() },
    },
    contact: {
      namespaced: true,
      getters: { successfullySent: vi.fn(), msgErrorRaised: vi.fn() },
    },
  },
};

// mount function from @vue/test-utils
// needs this enhancement to render vuetify components correctly
// source: https://vuetifyjs.com/en/getting-started/unit-testing/#mocking-vuetify

export const getMountWithVuetify = () => {
  const vuetify = createVuetify({
    components,
    directives,
  });

  return nativeMount({
    props: {},
    global: {
      components: {
        HacknightWrapper,
        HacknightsParticipants,
        DashboardHeader,
        ParticipantsSearch,
        ParticipantsList,
        ParticipantsChart,
        DashboardMain,
        AboutUs,
        ContactUs,
        HomePageHeader,
        JoinUs,
        OurProjects,
        ModalContent,
        PageFooter,
        SocialMedia,
        HomePage,
        LoginForm,
      },
      plugins: [vuetify],
    },
  });
};

// mount function from @vue/test-utils
// needs this enhancement to render components using vuex correctly
// source: https://vue-test-utils.vuejs.org/guides/using-with-vuex.html

export const getMountWithVuex = () => {
  const store = createStore(storeObject);

  return nativeMount({
    props: {},
    global: {
      components: {
        HacknightWrapper,
        HacknightsParticipants,
        DashboardHeader,
        ParticipantsSearch,
        ParticipantsList,
        ParticipantsChart,
        DashboardMain,
        AboutUs,
        ContactUs,
        HomePageHeader,
        JoinUs,
        OurProjects,
        ModalContent,
        PageFooter,
        SocialMedia,
        HomePage,
        LoginForm,
      },
      plugins: [store],
    },
  });
};

// Use this function if you need to test a component
// that uses both Vuex and Vuetify

export const getMountWithProviders = () => {
  const store = createStore(storeObject);
  const vuetify = createVuetify({
    components,
    directives,
  });

  return nativeMount({
    props: {},
    global: {
      components: {
        HacknightWrapper,
        HacknightsParticipants,
        DashboardHeader,
        ParticipantsSearch,
        ParticipantsList,
        ParticipantsChart,
        DashboardMain,
        AboutUs,
        ContactUs,
        HomePageHeader,
        JoinUs,
        OurProjects,
        ModalContent,
        PageFooter,
        SocialMedia,
        HomePage,
        LoginForm,
      },
      plugins: [store, vuetify],
    },
  });
};
