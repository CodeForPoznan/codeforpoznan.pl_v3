<template>
  <div class="register-form">
    <v-app id="login">
      <v-layout justify-center>
        <v-flex xs12 sm6>
          <v-alert
            type="error"
            :value="!!getError"
            dismissible
            transition="slide-y-transition"
            >{{ getError }}</v-alert
          >
          <v-alert
            type="success"
            :value="successAlert"
            @click="successAlert = !successAlert"
            transition="slide-y-transition"
            >Pomyślnie zalogowano</v-alert
          >
          <v-progress-circular
            v-if="showSpinner"
            :size="50"
            color="green"
            indeterminate
          >
          </v-progress-circular>
          <form @keyup.enter="onSubmit">
            <v-text-field
              v-model="github_username"
              label="Nazwa użytkownika"
              required
              :error-messages="githubUsernameErrors"
              @input="v$.github_username.$touch()"
              @blur="v$.github_username.$touch()"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Hasło"
              :append-icon="showPassword ? 'visibility_off' : 'visibility'"
              :type="showPassword ? 'text' : 'password'"
              @click:append="showPassword = !showPassword"
              required
              :error-messages="passwordErrors"
              @input="v$.password.$touch()"
              @blur="v$.password.$touch()"
            ></v-text-field>
            <v-btn @click="onSubmit">Zaloguj</v-btn>
          </form>
        </v-flex>
      </v-layout>
    </v-app>
  </div>
</template>

<script>
import { minLength, required } from '@vuelidate/validators';
import { mapGetters } from 'vuex';
import { useVuelidate } from '@vuelidate/core';

export default {
  setup() {
    return {
      v$: useVuelidate(),
    };
  },
  data() {
    return {
      github_username: '',
      password: '',
      showPassword: false,
      successAlert: false,
      showSpinner: false,
    };
  },

  validations: {
    github_username: { required, minLength: minLength(3) },
    password: { required },
  },

  methods: {
    onSubmit() {
      const loginData = {
        github_username: this.github_username,
        password: this.password,
      };

      if (!this.v$.$invalid) {
        this.showSpinner = true;
        this.$store.dispatch('auth/login', loginData).then((status) => {
          this.showSpinner = false;
          this.clearForm();
          if (status == 201) {
            this.successAlert = true;
          }
        });
      }
    },
    clearForm() {
      this.v$.$reset();
      this.github_username = '';
      this.password = '';
    },
  },

  computed: {
    githubUsernameErrors() {
      const errors = [];

      if (!this.v$.github_username.$dirty) return errors;
      !this.v$.github_username.minLength &&
        errors.push('Wprowadź poprawną nazwę użytkownika');
      !this.v$.github_username.required &&
        errors.push('Nazwa użytkownika jest wymagana');
      return errors;
    },
    passwordErrors() {
      const errors = [];

      if (!this.v$.password.$dirty) return errors;
      !this.v$.password.required && errors.push('Hasło jest wymagane');
      return errors;
    },
    ...mapGetters('auth', ['getError', 'isLoggedIn']),
  },
};
</script>

<style lang="scss" scoped>
@import '../../main.scss';
.v-messages__message {
  padding: 2px;
}
#login {
  margin-top: 20vh;
  margin-left: 2em;
  margin-right: 2em;
}
</style>
