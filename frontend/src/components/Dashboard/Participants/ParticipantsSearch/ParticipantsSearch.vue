<template>
  <!-- eslint-disable -->
  <v-autocomplete
    clearable
    variant="outlined"
    label="Search participants"
    :items="sortedParticipants"
    :item-title="displayText"
    item-value="first_name"
    v-model="selectedParticipant"
    :return-object="true"
  >
    <template v-slot:no-data>
      <v-list-item>
        <v-list-item-title>
          No results matching "<strong>{{ search }}</strong
          >".
        </v-list-item-title>
      </v-list-item>
    </template>
  </v-autocomplete>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  props: {
    value: {
      type: Object,
    },
  },
  computed: {
    ...mapGetters('participant', {
      getParticipants: 'getParticipants',
    }),
    sortedParticipants() {
      const participants = this.getParticipants;

      return participants.sort((a, b) =>
        a.first_name.localeCompare(b.github_username)
      );
    },
    selectedParticipant: {
      get() {
        return this.value;
      },
      set(selectedParticipant) {
        const newSelectedParticipant =
          typeof selectedParticipant === 'object' ? selectedParticipant : null;
        this.$emit('input', newSelectedParticipant);
      },
    },
  },
  methods: {
    filterParticipants(item, queryText) {
      console.log(item);
      console.log(queryText);
      return Object.values(item).some(
        (value) =>
          value &&
          value.toString().toLowerCase().includes(queryText.toLowerCase())
      );
    },
    displayText(participant) {
      const { first_name, last_name, slack, github_username } = participant;

      return `${first_name} ${last_name} (${slack || ''}/${github_username})`;
    },
  },
};
</script>
