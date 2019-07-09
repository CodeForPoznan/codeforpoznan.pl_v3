<template>
    <div>
        <v-app>
            <v-container>
                <form @submit.prevent="onSubmit">
                    <v-text-field
                        v-model="name"
                        :error-messages="nameErrors"
                        label="Imię"
                        required
                        @input="$v.name.$touch()"
                        @blur="$v.name.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="email"
                        :error-messages="emailErrors"
                        label="E-mail"
                        required
                        @input="$v.email.$touch()"
                        @blur="$v.email.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="phone_no"
                        mask="###-###-###"
                        :error-messages="phoneErrors"
                        :counter="9"
                        label="Telefon"
                        @input="$v.phone_no.$touch()"
                        @blur="$v.phone_no.$touch()"
                    ></v-text-field>
                    <v-textarea
                        v-model="content"
                        :error-messages="contentErrors"
                        label="Wiadomość"
                        required
                        @input="$v.content.$touch()"
                        @blur="$v.content.$touch()"
                    ></v-textarea>
                    <v-btn type="submit" :disabled="$v.$invalid" color="info"
                        >Wyślij</v-btn
                    >
                </form>
            </v-container>
        </v-app>
    </div>
</template>

<script>
import {
    required,
    email,
    maxLength,
    minLength
} from 'vuelidate/lib/validators';

export default {
    data() {
        return {
            name: '',
            email: '',
            phone_no: '',
            content: ''
        };
    },
    methods: {
        onSubmit() {
            const contactData = {
                name: this.name,
                email: this.email,
                phone: this.phone_no,
                content: this.content
            };

            if (!this.$v.$invalid) {
                this.$store.dispatch('contact/sentMessage', contactData).then(
                    response => {
                        if (response.status == 200) this.resetForm();
                    },
                    () => {
                        this.$store.commit('contact/raiseMsgError');
                    }
                );
            }
        },
        resetForm() {
            this.$v.$reset();
            this.name = '';
            this.email = '';
            this.phone_no = '';
            this.content = '';
        }
    },
    validations: {
        name: { required, maxLength: maxLength(50) },
        email: { required, email },
        phone_no: { minLength: minLength(9), maxLength: maxLength(9) },
        content: {
            required,
            minLength: minLength(10),
            maxLength: maxLength(2000)
        }
    },
    computed: {
        nameErrors() {
            const errors = [];

            if (!this.$v.name.$dirty) return errors;
            !this.$v.name.required && errors.push('Imię jest wymagane');
            return errors;
        },
        emailErrors() {
            const errors = [];

            if (!this.$v.email.$dirty) return errors;
            !this.$v.email.email &&
                errors.push('Poprawny adres email jest wymagany');
            !this.$v.email.required && errors.push('E-mail jest wymagany');
            return errors;
        },
        phoneErrors() {
            const errors = [];

            !this.$v.phone_no.minLength &&
                errors.push('Wprowadź poprawny numer np. 111-222-333');
            return errors;
        },
        contentErrors() {
            const errors = [];

            if (!this.$v.content.$dirty) return errors;
            !this.$v.content.minLength &&
                errors.push('Minimalna długość to 10 znaków');
            !this.$v.content.required &&
                errors.push('Treść wiadomości jest wymagana');
            return errors;
        }
    }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';
</style>
