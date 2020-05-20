<template>
  <v-form>
    <v-text-field v-model="form.first_name" label="First name" />
    <v-text-field v-model="form.last_name" label="Last name" />
    <v-text-field v-model="form.email" label="E-mail" />
    <v-text-field v-model="form.phone" label="Phone No." />
    <v-text-field v-model="form.github" label="Github nick" />
    <v-text-field v-model="form.slack" label="Slack nick" />
    <v-btn @click="onSubmit">Add new participant</v-btn>
  </v-form>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        email: '',
        github: '',
        phone: '',
        slack: ''
      }
    };
  },
  created() {
    this.$store.dispatch('participant/getParticipants');
  },
  methods: {
    // validateEmail() {
    //   if (this.email = $store.allParticipants) {
    //     this.$v.$invalid()
    //   },
    // },
    onSubmit() {
      const newParticipantData = this.form;

      this.$store.dispatch('participant/createParticipant', newParticipantData);
    }
  },
  computed: {
    ...mapGetters('participant', ['getParticipants', 'error'])
  }
};
</script>

<style lang="scss" scoped></style>
