<template>
  <v-container fluid text-xs-center>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="6">
        <v-alert
          type="error"
          :value="!!getError"
          transition="slide-y-transition"
          dismissible
          >{{ getError }}</v-alert
        >
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="6">
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
              class="add-hacknight-btn"
              @click="datePicker = true"
              offset-y
            >
              <v-icon left dark>mdi-plus</v-icon>
              New
            </v-btn>
          </template>
        </v-select>
      </v-col>
    </v-row>
    <v-dialog v-model="datePicker" max-width="500">
      <v-card>
        <v-card-title></v-card-title>
        <v-card-text>
          <v-date-picker
            v-model="date"
            show-adjacent-months
            :max="getTodayDate"
            color="#0CAEE7"
            @dblclick:date="onCreateHacknight"
            :allowed-dates="allowedDates"
            full-width
          ></v-date-picker>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="#607d8b"
            text
            @click="
              onCreateHacknight(date);
              datePicker = false;
            "
          >
            Create
          </v-btn>
          <v-btn color="#607d8b" text @click="datePicker = false">
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  data() {
    return {
      selectedHacknight: null,
      date: null,
      datePicker: false
    };
  },
  created() {
    this.$store.dispatch('hacknight/getHacknights');
    this.date = this.getTodayDate;
  },
  methods: {
    onCreateHacknight(date = this.date) {
      this.$store
        .dispatch('hacknight/createHacknight', date)
        .then(() => (this.selectedHacknight = this.getHacknight));
    },
    onGetHacknight() {
      this.$store.dispatch('hacknight/getHacknight', this.selectedHacknight);
    },
    allowedDates(val) {
      const hacknightDates = this.getHacknights.flatMap(({ date }) => [date]);

      return !hacknightDates.includes(val);
    }
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknights', 'getHacknight', 'getError']),
    getTodayDate() {
      return new Date().toISOString().slice(0, 10);
    }
  }
};
</script>
<style lang="scss" scoped>
@import '../../../main.scss';
.add-hacknight-btn {
  top: -12px;
  margin: 8px;
  color: #ffffff;
  caret-color: #ffffff;
  background-color: #607d8b !important;
  border-color: #607d8b;
}
</style>
