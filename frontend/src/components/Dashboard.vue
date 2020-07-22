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
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import DashboardHeader from './DashboardHeader.vue';
import Hacknight from './Hacknight.vue';
import Participants from './Participants.vue';
import HacknightsParticipants from './HacknightsParticipants.vue';

export default {
  components: {
    'app-dashboard-header': DashboardHeader,
    'app-hacknight': Hacknight,
    'app-hacknights-participants': HacknightsParticipants,
    'app-participants': Participants
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknight'])
  }
};
</script>

<style lang="scss" scoped></style>
