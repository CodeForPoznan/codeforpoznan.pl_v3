<template>
  <v-container fluid text-xs-center>
    <v-row align="center" justify="center">
      <v-col class="d-flex" cols="12" sm="6">
        <v-select
          v-model="selectedHacknight"
          :items="hacknights"
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
export default {
  data() {
    return {
      selectedHacknight: '',
      hacknight: {},
      hacknights: []
    };
  },
  created() {
    this.$store.dispatch('hacknight/getHacknights').then(res => {
      this.hacknights = res.data.hacknights;
    });
  },
  methods: {
    onCreateHacknight() {
      this.$store.dispatch('hacknight/createHacknight').then(res => {
        this.hacknight = res.data.hacknight;
        this.hacknights.push(this.hacknight);
        this.selectedHacknight = this.hacknight.id;
      });
    },
    onGetHacknight() {
      this.$store
        .dispatch('hacknight/getHacknight', this.selectedHacknight)
        .then(res => {
          this.hacknight = res.data;
        });
    }
  }
};
</script>
<style lang="scss" scoped>
@import './../main.scss';
</style>
