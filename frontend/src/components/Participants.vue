<template>
  <v-form>
    <v-text-field v-model="first_name" label="First name" />
    <v-text-field v-model="last_name" label="Last name" />
    <v-text-field v-model="email" label="E-mail" />
    <v-text-field v-model="phone" label="Phone No." />
    <v-text-field v-model="github" label="Github nick" />
    <v-text-field v-model="slack" label="Slack nick" />
    <v-btn @click="onSubmit">Add new participant</v-btn>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      github: '',
      phone: '',
      slack: ''
    };
  },
  methods: {
    onSubmit() {
      const newParticipantData = {[
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        github: this.github,
        phone: this.phone,
        slack: this.slack,
      ]};

      this.$store.dispatch('participant/createParticipant', newParticipantData);
    }
  }
};
</script>

<style lang="scss" scoped></style>
