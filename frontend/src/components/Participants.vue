<template>
  <v-container>
    <v-form>
      <v-text-field
        type="text"
        label="E-mail"
        v-model.trim="form.email"
        @blur="$v.form.email.$touch()"
        :error-messages="emailErrors"
        required
      />
      <v-text-field
        label="Github link"
        v-model="form.githubLink"
        @blur="$v.form.githubLink.$touch()"
        :error-messages="githubErrors"
        required
      />
      <v-text-field
        v-model="form.firstName"
        label="First name"
        @blur="$v.form.firstName.$touch()"
        :error-messages="githubErrors"
        required
      />
      <v-text-field v-model="form.lastName" label="Last name" />
      <v-text-field v-model="form.slack" label="Slack nick" />
      <v-text-field v-model="form.phone" label="Phone No." />
      <v-btn type="submit" :disabled="$v.$invalid" @click="onSubmit"
        >Add new participant</v-btn
      >
    </v-form>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import {
  required,
  minLength,
  maxLength,
  email,
  url
} from 'vuelidate/lib/validators';
export default {
  data() {
    return {
      form: {
        email: '',
        githubLink: '',
        firstName: '',
        lastName: '',
        slack: '',
        phone: ''
      }
    };
  },
  created() {
    this.$store.dispatch('participant/getParticipants');
  },
  validations: {
    form: {
      email: {
        required,
        email,
        emailExists(value) {
          return !Object.values(this.allParticipants).find(
            user => user.email === value
          );
        }
      },
      githubLink: {
        required,
        url,
        githubExists(value) {
          return !Object.values(this.allParticipants).find(
            user => user.github === value
          );
        }
      },
      firstName: {
        required,
        minLength: minLength(3),
        maxLength: maxLength(25)
      }
    }
  },
  methods: {
    onSubmit() {
      const newParticipantData = this.form;

      this.$store.dispatch('participant/createParticipant', newParticipantData);
    }
  },
  computed: {
    ...mapState('participant', {
      allParticipants: 'allParticipants'
    }),
    emailErrors() {
      const errors = [];

      if (!this.$v.form.email.$dirty) return errors;
      !this.$v.form.email.required && errors.push('This field is required');
      !this.$v.form.email.email && errors.push('Type a correct e-mail address');
      !this.$v.form.email.emailExists && errors.push('User already exists');
      return errors;
    },
    githubErrors() {
      const errors = [];

      if (!this.$v.form.githubLink.$dirty) return errors;
      !this.$v.form.githubLink.required &&
        errors.push('This field is required');
      !this.$v.form.githubLink.url &&
        errors.push('This field requires URL link to a github account');
      !this.$v.form.githubLink.githubExists &&
        errors.push('User already exists');
      return errors;
    },
    firstNameErrors() {
      const errors = [];

      if (!this.$v.form.firstName.$dirty) return errors;
      !this.$v.form.firstName.required && errors.push('This field is required');
      !this.$v.form.firstName.minLength && errors.push('Name is too short');
      !this.$v.form.firstName.maxLength && errors.push('Name is too long');
      return errors;
    }
  }
};
</script>

<style lang="scss" scoped></style>
