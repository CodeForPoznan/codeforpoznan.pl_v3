<template>
  <div class="register-form">
    <v-app id="login">
      <v-container class="align-center d-flex" fill-height fluid>
        <v-col>
          <v-row class="d-flex justify-center mb-6">
            <v-col cols="12" xs="12" sm="6">
              <v-alert
                type="error"
                :model-value="!!getError"
                :text="getError"
                closable
                transition="slide-y-transition"
              ></v-alert>
              <v-alert
                type="success"
                :model-value="successAlert"
                text="Pomyślnie zalogowano"
                closable
                @click="successAlert = !successAlert"
                transition="slide-y-transition"
              ></v-alert>
              <v-progress-circular
                v-if="showSpinner"
                :size="50"
                color="green"
                indeterminate
              >
              </v-progress-circular>
            </v-col>
          </v-row>
          <v-row class="d-flex justify-center mb-6">
            <v-col cols="12" xs="12" sm="6">
              <form @keyup.enter="onSubmit">
                <v-text-field
                  variant="underlined"
                  color="#0CAEE7"
                  v-model="loginForm.github_username"
                  label="Nazwa użytkownika"
                  required
                  :error-messages="
                    v$.loginForm.github_username.$errors.map((e) => e.$message)
                  "
                  @input="v$.loginForm.github_username.$touch()"
                  @blur="v$.loginForm.github_username.$touch()"
                ></v-text-field>
                <v-text-field
                  variant="underlined"
                  color="#0CAEE7"
                  v-model="loginForm.password"
                  label="Hasło"
                  :append-icon="
                    showPassword ? 'fa:fas fa-eye-slash' : 'fa:fas fa-eye'
                  "
                  :type="showPassword ? 'text' : 'password'"
                  @click:append="showPassword = !showPassword"
                  required
                  :error-messages="
                    v$.loginForm.password.$errors.map((e) => e.$message)
                  "
                  @input="v$.loginForm.password.$touch()"
                  @blur="v$.loginForm.password.$touch()"
                ></v-text-field>
                <v-btn @click="onSubmit" id="login-button">Zaloguj</v-btn>
              </form>
            </v-col>
          </v-row>
        </v-col>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import { minLength, required } from '@vuelidate/validators';
import { mapGetters } from 'vuex';
import { useVuelidate } from '@vuelidate/core';
import { reactive } from 'vue';

export default {
  setup() {
    const loginForm = reactive({
      github_username: '',
      password: '',
    });

    return {
      v$: useVuelidate(),
      loginForm,
    };
  },
  data() {
    return {
      showPassword: false,
      successAlert: false,
      showSpinner: false,
    };
  },

  validations: {
    loginForm: {
      github_username: { required, minLength: minLength(3) },
      password: { required },
    },
  },

  methods: {
    onSubmit() {
      const loginData = {
        github_username: this.loginForm.github_username,
        password: this.loginForm.password,
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
      this.loginForm.github_username = '';
      this.loginForm.password = '';
    },
  },

  computed: {
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
#login-button {
  background: $blue;
  color: $white;
}
</style>
