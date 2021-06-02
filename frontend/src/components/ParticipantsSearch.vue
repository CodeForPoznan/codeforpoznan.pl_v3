<template>
  <v-combobox
    clearable
    label="Search participants"
    :items="sortedParticipants"
    item-text="github"
    :filter="filterParticipants"
    v-model="selectedParticipant"
  ></v-combobox>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  props: {
    value: {
      type: Object | null,
      required: true
    }
  },
  computed: {
    ...mapGetters('participant', {
      getParticipants: 'getParticipants'
    }),
    sortedParticipants() {
      return this.getParticipants.sort((a, b) =>
        a.github.localeCompare(b.github)
      );
    },
    selectedParticipant: {
      get() {
        return this.value;
      },
      set(selectedParticipant) {
        this.$emit('input', selectedParticipant);
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
    }
  }
};
</script>
