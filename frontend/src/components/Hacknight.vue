<template>
  <v-container fluid text-xs-center>
    <v-row align="center" justify="center">
      <v-col class="d-flex" cols="12" sm="6">
        <v-alert
          type="error"
          :value="getError ? true : false"
          transition="slide-y-transition"
          dismissible
          >{{ getError }}</v-alert
        >
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col class="d-flex" cols="12" sm="6">
        <v-select
          v-model="selectedHacknight"
          :items="getHacknights"
          item-text="date"
          item-value="id"
          label="Select Hacknight"
          @input="onGetHacknight"
        >
          <template v-slot:append-outer>
            <v-btn
              color="blue-grey"
              class="ma-2 white--text"
              @click="onCreateHacknight"
              style="top: -12px"
              offset-y
            >
              <v-icon left dark>mdi-plus</v-icon>
              New
            </v-btn>
          </template>
        </v-select>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  data() {
    return {
      selectedHacknight: null
    };
  },
  created() {
    this.$store.dispatch('hacknight/getHacknights');
  },
  methods: {
    onCreateHacknight() {
      this.$store
        .dispatch('hacknight/createHacknight')
        .then(() => (this.selectedHacknight = this.getHacknight));
    },
    onGetHacknight() {
      this.$store.dispatch('hacknight/getHacknight', this.selectedHacknight);
    }
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknights', 'getHacknight', 'getError'])
  }
};
</script>
<style lang="scss" scoped>
@import './../main.scss';
</style>
