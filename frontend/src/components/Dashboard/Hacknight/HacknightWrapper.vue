<template>
  <v-container fluid text-xs-center class="pt-6">
    <v-row align="center" justify="center" class="pt-6">
      <v-col cols="12" sm="6">
        <v-alert
          type="error"
          :model-value="!!getError"
          :text="getError"
          transition="slide-y-transition"
          closable
        ></v-alert>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col cols="10" sm="4" align-self="end">
        <v-select
          v-model="selectedHacknight"
          color="#0CAEE7"
          variant="underlined"
          :items="getHacknights"
          item-title="date"
          item-value="id"
          label="Select Hacknight"
          @update:modelValue="onGetHacknight"
        >
        </v-select>
      </v-col>
      <v-col cols="2" sm="2" align-self="end">
        <v-btn
          class="add-hacknight-btn"
          @click="datePicker = true"
          offset-y
          prepend-icon="fa:fas fa-plus"
        >
          New
        </v-btn>
      </v-col>
    </v-row>
    <v-dialog v-model="datePicker" max-width="500">
      <v-date-picker
        v-model="date"
        show-adjacent-months
        :max="getTodayDate"
        color="#0CAEE7"
        @click:save="
          onCreateHacknight();
          datePicker = false;
        "
        @click:cancel="datePicker = false"
        full-width
      ></v-date-picker>
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
      datePicker: false,
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
    },
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknights', 'getHacknight', 'getError']),
    getTodayDate() {
      return new Date().toISOString().slice(0, 10);
    },
  },
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
