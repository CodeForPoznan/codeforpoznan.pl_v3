<template>
  <v-container fluid text-xs-center>
    <v-row align="center" justify="center">
      <v-col class="d-flex" cols="12" lg="8" md="10">
        <v-combobox
          v-model="selectedParticipants"
          outlined
          :items="filerOutParticipants()"
          item-text="github"
          item-value="github"
          :search-input.sync="search"
          hide-selected
          label="Add participants"
          multiple
          small-chips
          clearable
          deletable-chips
          append-outer-icon="mdi-cloud-upload"
        >
          <template v-if="noData" v-slot:no-data>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>
                  No results matching "<strong>{{ search }}</strong
                  >".
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
          <template v-slot:append-outer>
            <v-btn
              color="blue-grey"
              class="ma-2 white--text add-hacknight-btn"
              :disabled="!selectedParticipants.length"
              @click="onAddParticipants"
              offset-y
            >
              <v-icon dark>mdi-cloud-upload</v-icon>
            </v-btn>
          </template>
        </v-combobox>
      </v-col>
    </v-row>
    <v-card class="mx-auto" color="white" max-width="500">
      <v-toolbar flat color="transparent">
        <v-avatar color="blue" size="48" style="margin-right:1em;">
          <span class="white--text headline">{{
            getHacknight.participants.length
          }}</span>
        </v-avatar>
        <v-toolbar-title>Participants</v-toolbar-title>
        <div class="flex-grow-1"></div>
      </v-toolbar>
      <v-divider v-if="getHacknight.participants"></v-divider>
      <v-list>
        <template v-for="(item, i) in orderedParticipants()">
          <v-list-item v-if="getHacknight.participants" :key="i">
            <v-list-item-avatar>
              <v-icon>mdi-account-outline</v-icon>
            </v-list-item-avatar>
            <v-list-item-title v-text="item.github"></v-list-item-title>
            <v-btn icon v-on:click="onDeleteParticipant(item)">
              <i class="button_delete fas fa-user-times fa-lg"></i>
            </v-btn>
          </v-list-item>
        </template>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex';
import _ from 'lodash';
export default {
  data() {
    return {
      selectedParticipants: [],
      search: null,
      noData: true
    };
  },
  methods: {
    onAddParticipants() {
      const ids = this.selectedParticipants.map(participant => participant.id);

      this.$store
        .dispatch('hacknight/addParticipants', ids)
        .then(() => (this.selectedParticipants = []));
    },
    onDeleteParticipant(participant) {
      const ids = [participant.id];

      this.$store.dispatch('hacknight/deleteParticipants', ids);
    },
    filerOutParticipants() {
      return this.getParticipants
        .filter(
          participant =>
            !this.getHacknight.participants.some(
              hacknightParticipant => hacknightParticipant.id === participant.id
            )
        )
        .sort((a, b) => a.github.localeCompare(b.github));
    },
    orderedParticipants() {
      return _.sortBy(this.getHacknight.participants, participant =>
        participant.github.toLowerCase()
      );
    }
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknight']),
    ...mapGetters('participant', ['getParticipants', 'error'])
  }
};
</script>
<style lang="scss" scoped>
@import '../../../main.scss';
.add-hacknight-btn {
  top: -12px;
}
.button_delete {
  color: $red;
}
</style>
