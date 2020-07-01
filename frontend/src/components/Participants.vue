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
import { mapState } from 'vuex';
import { minLength, maxLength, required } from 'vuelidate/lib/validators';
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
  validations: {
    form: {
      first_name: {
        required,
        minLength: minLength(3),
        maxLength: maxLength(100)
      }
    }
  },
  methods: {
    onSubmit() {
      const newParticipantData = this.form;

      this.$store.dispatch('participant/createParticipant', newParticipantData);
    },
    validateEmail(event) {
      const formEmail = event.target.value;
      const userExist = !!Object.values(this.allParticipants).find(
        user => user.email === formEmail
      );

      return userExist;
      // console.log('userExist', userExist);
    }
  },
  computed: {
    ...mapState('participant', {
      allParticipants: 'allParticipants'
    })
  }
};
</script>

<style lang="scss" scoped></style>
