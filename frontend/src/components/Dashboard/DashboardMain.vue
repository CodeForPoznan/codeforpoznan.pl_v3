<template>
  <div>
    <v-row>
      <v-col>
        <app-dashboard-header />
      </v-col>
    </v-row>
    <v-row align="baseline">
      <v-col>
        <app-hacknight />
        <app-hacknights-participants v-if="getHacknight" />
      </v-col>
      <v-col>
        <app-participants />
      </v-col>
    </v-row>
    <v-row>
      <v-col class="d-flex justify-center">
        <ParticipantsChart />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import DashboardHeader from './Header/DashboardHeader.vue';
import HacknightWrapper from './Hacknight/HacknightWrapper.vue';
import ParticipantsList from './Participants/ParticipantsList.vue';
import HacknightsParticipants from './HacknightsParticipants/HacknightsParticipants.vue';
import ParticipantsChart from './ParticipantsChart/ParticipantsChart.vue';

export default {
  components: {
    'app-dashboard-header': DashboardHeader,
    'app-hacknight': HacknightWrapper,
    'app-hacknights-participants': HacknightsParticipants,
    'app-participants': ParticipantsList,
    ParticipantsChart,
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknight']),
  },
  created() {
    this.$store.dispatch('participant/getParticipants');
  },
};
</script>

<style lang="scss" scoped></style>
