<template>
  <v-container>
    <v-flex xs12 sm6>
      <v-alert
        v-if="successAlert"
        @click="successAlert = !successAlert"
        transition="slide-y-transition"
        >ok</v-alert
      >
    </v-flex>
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
        v-model="form.github"
        @blur="$v.form.github.$touch()"
        :error-messages="githubErrors"
        required
      />
      <v-text-field
        label="First name"
        v-model="form.first_name"
        @blur="$v.form.first_name.$touch()"
        :error-messages="firstNameErrors"
        required
      />
      <v-text-field
        label="Last name"
        v-model="form.last_name"
        @blur="$v.form.last_name.$touch()"
        :error-messages="lastNameErrors"
        required
      />
      <v-text-field
        label="Slack nick"
        v-model="form.slack"
        @blur="$v.form.slack.$touch()"
        :error-messages="slackErrors"
        required
      />
      <v-text-field v-model="form.phone" label="Phone No." />
      <v-btn :disabled="$v.$invalid" @click="onSubmit"
        >Add new participant</v-btn
      >
    </v-form>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import { mapGetters } from 'vuex';
import {
  required,
  minLength,
  maxLength,
  email
} from 'vuelidate/lib/validators';
export default {
  data() {
    return {
      form: {
        email: '',
        github: '',
        first_name: '',
        last_name: '',
        slack: '',
        phone: ''
      },
      slackExists: false,
      successAlert: false
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
      github: {
        required,
        githubExists(value) {
          return !Object.values(this.allParticipants).find(
            user => user.github === value
          );
        }
      },
      first_name: {
        required,
        minLength: minLength(3),
        maxLength: maxLength(25)
      },
      last_name: {
        required,
        minLength: minLength(3),
        maxLength: maxLength(25)
      },
      slack: {
        required,
        minLength: minLength(3),
        maxLength: maxLength(25)
      }
    }
  },
  methods: {
    onSubmit() {
      const newParticipantData = this.form;

      if (!this.$v.form.$invalid)
        this.$store
          .dispatch('participant/createParticipant', newParticipantData)
          .then(status => {
            this.clearForm();
            if (status == 201) {
              this.successAlert = true;
            }
          });
    },
    clearForm() {
      this.$v.form.$reset();
      this.form.email = '';
      this.form.github = '';
    }
  },
  computed: {
    // ...mapGetters('participants', ['getParticipants', 'raiserError'])
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

      if (!this.$v.form.github.$dirty) return errors;
      !this.$v.form.github.required && errors.push('This field is required');
      !this.$v.form.github.githubExists && errors.push('User already exists');
      return errors;
    },
    firstNameErrors() {
      const errors = [];

      if (!this.$v.form.first_name.$dirty) return errors;
      !this.$v.form.first_name.required &&
        errors.push('This field is required');
      !this.$v.form.first_name.minLength && errors.push('Name is too short');
      !this.$v.form.first_name.maxLength && errors.push('Name is too long');
      return errors;
    },
    lastNameErrors() {
      const errors = [];

      if (!this.$v.form.last_name.$dirty) return errors;
      !this.$v.form.last_name.required && errors.push('This field is required');
      !this.$v.form.last_name.minLength && errors.push('Name is too short');
      !this.$v.form.last_name.maxLength && errors.push('Name is too long');
      return errors;
    },
    slackErrors() {
      const errors = [];

      if (!this.$v.form.slack.$dirty) return errors;
      !this.$v.form.slack.required && errors.push('This field is required');
      !this.$v.form.slack.minLength && errors.push('Name is too short');
      !this.$v.form.slack.maxLength && errors.push('Name is too long');
      return errors;
    }
  }
};
</script>

<style lang="scss" scoped></style>
