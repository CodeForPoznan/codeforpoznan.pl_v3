<template>
  <div>
    <app-dashboard-header />
    <app-hacknight />
    <app-hacknights-participants v-if="getHacknight" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import DashboardHeader from './DashboardHeader.vue';
import Hacknight from './Hacknight.vue';
import HacknightsParticipants from './HacknightsParticipants.vue';

export default {
  components: {
    'app-dashboard-header': DashboardHeader,
    'app-hacknight': Hacknight,
    'app-hacknights-participants': HacknightsParticipants
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknight'])
  }
};
</script>

<style lang="scss" scoped></style>
