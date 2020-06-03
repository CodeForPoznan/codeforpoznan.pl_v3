<template>
  <v-container>
    <v-form>
      <v-text-field v-model="form.first_name" label="First name" />
      <v-text-field v-model="form.last_name" label="Last name" />
      <v-text-field
        v-model="form.email"
        @blur="validateEmail($event)"
        error-messages="kk"
        label="E-mail"
      />
      <v-text-field v-model="form.phone" label="Phone No." />
      <v-text-field v-model="form.github" label="Github nick" />
      <v-text-field v-model="form.slack" label="Slack nick" />
      <v-btn @click="onSubmit">Add new participant</v-btn>
    </v-form>
  </v-container>
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
      },
      registeredEmails: []
    };
  },
  created() {
    this.$store.dispatch('participant/getParticipants');
  },
  methods: {
    onSubmit() {
      const newParticipantData = this.form;

      this.$store.dispatch('participant/createParticipant', newParticipantData);
    },
    validateEmail(event) {
      this.email = event.target.value;
      // console.log(event.target.value);
      this.registeredEmails = this.$store.getters.getEmails;
      // console.log(this.registeredEmails);

      if (this.email === this.registeredEmails) {
        this.invalidEmail = true;
      } else {
        this.invalidEmail = false;
        // console.log(this.invalidEmail);
      }
    }
  },
  computed: {
    ...mapGetters(['getEmails'])
  }
};
</script>

<style lang="scss" scoped></style>
