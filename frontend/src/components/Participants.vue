<template>
  <v-container class="pa-6">
    <v-flex>
      <v-alert
        type="error"
        :value="!!getError"
        dismissible
        transition="slide-y-transition"
        >{{ getError }}</v-alert
      >
      <v-alert
        type="warning"
        :value="warningAlert"
        v-model="warningAlert"
        dismissible
        @click="warningAlert = !warningAlert"
        transition="slide-y-transition"
        >{{ warningMessage }}</v-alert
      >
      <v-alert
        type="success"
        :value="successAlert"
        v-model="successAlert"
        dismissible
        @click="successAlert = !successAlert"
        transition="slide-y-transition"
        >Participant has been successfully added</v-alert
      >
    </v-flex>
    <v-card>
      <v-toolbar flat>
        <v-icon class="pa-3">fas fa-user-plus</v-icon>
        <v-toolbar-title>Create new participant</v-toolbar-title>
      </v-toolbar>
      <v-divider></v-divider>
      <v-form @keyup.enter="onSubmit" class="pa-6" ref="form">
        <v-text-field
          type="text"
          label="E-mail"
          v-model.trim="form.email"
          @blur="$v.form.email.$touch()"
          :error-messages="emailErrors"
        />
        <v-text-field
          label="Github link"
          v-model="form.github"
          @blur="$v.form.github.$touch()"
          :error-messages="githubErrors"
        />
        <v-text-field
          label="First name"
          v-model="form.first_name"
          @blur="$v.form.first_name.$touch()"
          :error-messages="firstNameErrors"
        />
        <v-text-field
          label="Last name"
          v-model="form.last_name"
          @blur="validateLastName($event)"
          :error-messages="lastNameErrors"
        />
        <v-text-field
          label="Slack nick"
          v-model="form.slack"
          @blur="validateSlack($event)"
          :error-messages="slackErrors"
        />
        <v-text-field
          label="Phone No."
          v-model="form.phone"
          :counter="9"
          @blur="validatePhone($event)"
          :error-messages="phoneErrors"
        />
        <v-card-actions class="pt-3 align-center justify-center">
          <v-btn
            :disabled="$v.$invalid"
            @click="onSubmit"
            class="add-participant-btn align-center justify-center"
            >Add new participant</v-btn
          >
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import { mapState } from 'vuex';
import { mapGetters } from 'vuex';
import {
  required,
  minLength,
  maxLength,
  email,
  numeric
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
      warningAlert: false,
      warningMessage: '',
      successAlert: false
    };
  },
  created() {
    this.$store.dispatch('participant/getParticipants');
    setInterval(() => {
      this.successAlert = false;
    }, 10000);
    setInterval(() => {
      this.warningAlert = false;
    }, 30000);
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
        minLength: minLength(3),
        maxLength: maxLength(25)
      },
      phone: {
        numeric,
        minLength: minLength(9),
        maxLength: maxLength(9)
      }
    }
  },
  methods: {
    onSubmit() {
      if (!this.$v.form.$invalid) {
        if (this.form.phone === '') this.form.phone = '111111111';
        if (this.form.slack === '') this.form.slack = 'brak';
        const newParticipantData = this.form;

        this.$store
          .dispatch('participant/createParticipant', newParticipantData)
          .then(status => {
            if (status === 201) {
              this.successAlert = true;
              this.$refs.form.reset();
              this.$v.form.$reset();
            }
          });
      }
    },
    validateSlack($event) {
      this.$v.form.slack.$touch();
      if (
        Object.values(this.allParticipants).find(
          user => user.slack === $event.target.value
        )
      )
        this.warningAlert = true;
      this.warningMessage =
        'This slack nick already exists. Please suggest change of the nick to avoid confusion on Slack';
    },
    validateLastName($event) {
      this.$v.form.slack.$touch();
      if (
        Object.values(this.allParticipants).find(
          user => user.last_name === $event.target.value
        )
      )
        this.warningAlert = true;
      this.warningMessage =
        'This last name already exists. Please verify if a person is actually a new paricipant';
    },
    validatePhone($event) {
      this.$v.form.phone.$touch();
      if (
        Object.values(this.allParticipants).find(
          user => user.phone === $event.target.value
        )
      )
        this.warningAlert = true;
      this.warningMessage =
        'This phone number already exists. Please verify if a person is actually a new paricipant';
    }
  },
  computed: {
    ...mapGetters('participant', ['getError']),
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
      !this.$v.form.last_name.minLength &&
        errors.push('Last name is too short');
      !this.$v.form.last_name.maxLength && errors.push('Last name is too long');
      return errors;
    },
    slackErrors() {
      const errors = [];

      if (!this.$v.form.slack.$dirty) return errors;
      !this.$v.form.slack.minLength && errors.push('Nick is too short');
      !this.$v.form.slack.maxLength && errors.push('Nick is too long');
      return errors;
    },
    phoneErrors() {
      const errors = [];

      if (!this.$v.form.phone.$dirty) return errors;
      !this.$v.form.phone.numeric &&
        errors.push('You can only type digits here');
      !this.$v.form.phone.minLength &&
        errors.push('Type correct number ie. 111-222-333');
      !this.$v.form.phone.maxLength &&
        errors.push('Type correct number ie. 111-222-333');
      return errors;
    }
  }
};
</script>

<style lang="scss" scoped>
.add-participant-btn {
  color: #ffffff;
  caret-color: #ffffff;
  background-color: #607d8b !important;
  border-color: #607d8b;
}
</style>
