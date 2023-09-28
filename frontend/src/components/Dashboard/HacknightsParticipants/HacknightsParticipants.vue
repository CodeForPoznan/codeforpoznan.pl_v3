<template>
  <v-container fluid text-xs-center>
    <v-row align="center" justify="center">
      <v-col class="d-flex" cols="10" lg="8" md="18">
        <v-container fluid>
          <!-- eslint-disable -->
          <v-combobox
            v-model="selectedParticipants"
            variant="outlined"
            :items="filerOutParticipants()"
            item-title="github_username"
            item-value="github_username"
            v-model:search="search"
            hide-selected
            label="Add participants"
            multiple
            chips
            closable-chips
            clearable
            append-outer-icon="mdi-cloud-upload"
            :hide-no-data="false"
          >
            <template v-slot:no-data>
              <v-list-item>
                <v-list-item-title>
                  No results matching "<strong>{{ search }}</strong
                  >".
                </v-list-item-title>
              </v-list-item>
            </template>
          </v-combobox>
        </v-container>
      </v-col>
      <v-col class="d-flex" cols="2">
        <v-btn
          color="blue-grey"
          size="large"
          class="white--text add-hacknight-btn"
          :disabled="!selectedParticipants.length"
          @click="onAddParticipants"
          offset-y
        >
          <v-icon icon="mdi mdi-cloud-upload"></v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-card class="mx-auto" color="white" max-width="500">
      <v-toolbar flat color="transparent">
        <v-avatar class="ma-2" color="blue" size="48">
          <span class="white--text headline">{{
            getHacknight.participants.length
          }}</span>
        </v-avatar>
        <v-toolbar-title>Participants</v-toolbar-title>
        <div class="flex-grow-1"></div>
      </v-toolbar>
      <v-divider v-if="getHacknight.participants"></v-divider>
      <v-list>
        <v-list-item
          v-for="item in orderedParticipants()"
          :key="item.github_username"
          :title="item.github_username"
          prepend-icon="mdi mdi-account-outline"
        >
          <template v-slot:append>
            <v-btn variant="plain" v-on:click="onDeleteParticipant(item)">
              <i class="button_delete fas fa-user-times fa-lg"></i>
            </v-btn>
          </template>
        </v-list-item>
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
      noData: true,
    };
  },
  methods: {
    onAddParticipants() {
      const ids = this.selectedParticipants.map(
        (participant) => participant.id
      );

      this.$store
        .dispatch('hacknight/addParticipants', ids)
        .then(() => (this.selectedParticipants = []));
    },
    onDeleteParticipant(participant) {
      this.$store.dispatch('hacknight/deleteParticipants', participant.id);
    },
    filerOutParticipants() {
      return this.getParticipants
        .filter(
          (participant) =>
            !this.getHacknight.participants.some(
              (hacknightParticipant) =>
                hacknightParticipant.id === participant.id
            )
        )
        .sort((a, b) => a.github_username.localeCompare(b.github_username));
    },
    orderedParticipants() {
      return _.sortBy(this.getHacknight.participants, (participant) =>
        participant.github_username.toLowerCase()
      );
    },
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknight']),
    ...mapGetters('participant', ['getParticipants', 'error']),
  },
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
