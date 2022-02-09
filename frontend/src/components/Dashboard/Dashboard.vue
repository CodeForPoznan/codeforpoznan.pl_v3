<template>
  <div>
    <app-dashboard-header />
    <v-row xs12>
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
import Hacknight from './Hacknight/Hacknight.vue';
import Participants from './Participants/Participants.vue';
import HacknightsParticipants from './HacknightsParticipants/HacknightsParticipants.vue';
import ParticipantsChart from './ParticipantsChart/ParticipantsChart.vue';

export default {
  components: {
    'app-dashboard-header': DashboardHeader,
    'app-hacknight': Hacknight,
    'app-hacknights-participants': HacknightsParticipants,
    'app-participants': Participants,
    ParticipantsChart
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknight'])
  },
  created() {
    this.$store.dispatch('participant/getParticipants');
  }
};
</script>

<style lang="scss" scoped></style>
