<template src="./Login.html" />
<style src="./Login.css"/>

<script>
import { minLength, required } from 'vuelidate/lib/validators'

export default {
  data() {
    return {
      username: '',
      password: '',
      showPass: false,
      error_msg: '',
      successAlert: false,
      showSpinner: false
    }
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
      }
      this.error_msg = ''
      if(!this.$v.$invalid) {
        this.showSpinner = true
        this.$store.dispatch('auth/login', loginData)
        .then( res => {
          this.showSpinner = false
          this.clearForm()
          if (res.status == 201) this.successAlert = true;
        }, error => {
          this.showSpinner = false
          this.clearForm()
          const err = error.response.data.msg
          if (err == "Not authorized") {
            this.error_msg = "Nieprawidłowa nazwa użytkownika, lub hasło"
          } else if (err.includes('User already logged in')) {
            this.error_msg = "Jesteś już zalogowany"
          } else if (error) {
            this.error_msg = "Logowanie nie powiodło się"
          }
        })
      }
    },
    clearForm() {
      this.$v.$reset()
      this.username = ''
      this.password = ''
    }
  },

  computed: {
    usernameErrors() {
      const errors = []
      if (!this.$v.username.$dirty) return errors
      !this.$v.username.minLength && errors.push(
        'Wprowadź poprawną nazwę użytkownika'
      )
      !this.$v.username.required && errors.push(
        'Nazwa użytkownika jest wymagana'
      )
      return errors
    },
    passwordErrors() {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.required && errors.push(
        'Hasło jest wymagane'
      )
      return errors
    },
  },
}
</script>
