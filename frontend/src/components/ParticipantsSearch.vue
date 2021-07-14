<template>
  <v-combobox
    clearable
    label="Search participants"
    :items="sortedParticipants"
    :item-text="displayText"
    :filter="filterParticipants"
    v-model="selectedParticipant"
    :search-input.sync="search"
  >
    <template v-slot:no-data>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>
            No results matching "<strong>{{ search }}</strong
            >".
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </template>
  </v-combobox>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  props: {
    value: {
      type: Object
    }
  },
  computed: {
    ...mapGetters('participant', {
      getParticipants: 'getParticipants'
    }),
    sortedParticipants() {
      const participants = this.getParticipants;

      return participants.sort((a, b) => a.first_name.localeCompare(b.github));
    },
    selectedParticipant: {
      get() {
        return this.value;
      },
      set(selectedParticipant) {
        const newSelectedParticipant =
          typeof selectedParticipant === 'object' ? selectedParticipant : null;

        this.$emit('input', newSelectedParticipant);
      }
    }
  },
  methods: {
    filterParticipants(item, queryText) {
      return Object.values(item).some(
        value =>
          value &&
          value
            .toString()
            .toLowerCase()
            .includes(queryText.toLowerCase())
      );
    },
    displayText(participant) {
      const { first_name, last_name, slack, github } = participant;

      return `${first_name} ${last_name} (${slack}/${github})`;
    }
  }
};
</script>
