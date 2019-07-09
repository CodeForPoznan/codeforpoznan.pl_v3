<template>
    <div class="register-form">
        <v-app id="login">
            <v-layout justify-center>
                <v-flex xs12 sm6>
                    <v-alert
                        type="error"
                        :value="error_msg ? true : false"
                        @click="error_msg = ''"
                        transition="slide-y-transition"
                        >{{ error_msg }}</v-alert
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
                    <form>
                        <v-text-field
                            v-model="username"
                            label="Nazwa użytkownika"
                            required
                            :error-messages="usernameErrors"
                            @input="$v.username.$touch()"
                            @blur="$v.username.$touch()"
                        ></v-text-field>
                        <v-text-field
                            v-model="password"
                            label="Hasło"
                            :append-icon="
                                showPass ? 'visibility_off' : 'visibility'
                            "
                            :type="showPass ? 'text' : 'password'"
                            @click:append="showPass = !showPass"
                            required
                            :error-messages="passwordErrors"
                            @input="$v.password.$touch()"
                            @blur="$v.password.$touch()"
                        ></v-text-field>
                        <v-btn @click="onSubmit">Zaloguj</v-btn>
                    </form>
                </v-flex>
            </v-layout>
        </v-app>
    </div>
</template>

<script>
import { minLength, required } from 'vuelidate/lib/validators';

export default {
    data() {
        return {
            username: '',
            password: '',
            showPass: false,
            error_msg: '',
            successAlert: false,
            showSpinner: false
        };
    },

    validations: {
        username: { required, minLength: minLength(5) },
        password: { required }
    },

    methods: {
        onSubmit() {
            const loginData = {
                username: this.username,
                password: this.password
            };

            this.error_msg = '';
            if (!this.$v.$invalid) {
                this.showSpinner = true;
                this.$store.dispatch('auth/login', loginData).then(
                    res => {
                        this.showSpinner = false;
                        this.clearForm();
                        if (res.status == 201) this.successAlert = true;
                    },
                    error => {
                        this.showSpinner = false;
                        this.clearForm();
                        const err = error.response.data.msg;

                        if (err == 'Not authorized') {
                            this.error_msg =
                                'Nieprawidłowa nazwa użytkownika, lub hasło';
                        } else if (err.includes('User already logged in')) {
                            this.error_msg = 'Jesteś już zalogowany';
                        } else if (error) {
                            this.error_msg = 'Logowanie nie powiodło się';
                        }
                    }
                );
            }
        },
        clearForm() {
            this.$v.$reset();
            this.username = '';
            this.password = '';
        }
    },

    computed: {
        usernameErrors() {
            const errors = [];

            if (!this.$v.username.$dirty) return errors;
            !this.$v.username.minLength &&
                errors.push('Wprowadź poprawną nazwę użytkownika');
            !this.$v.username.required &&
                errors.push('Nazwa użytkownika jest wymagana');
            return errors;
        },
        passwordErrors() {
            const errors = [];

            if (!this.$v.password.$dirty) return errors;
            !this.$v.password.required && errors.push('Hasło jest wymagane');
            return errors;
        }
    }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';
.v-messages__message {
    padding: 2px;
}
#login {
    margin-top: 20vh;
    margin-left: 2em;
    margin-right: 2em;
}
</style>
