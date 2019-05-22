<template src="./HomePage.html" />

<script>
import { mapGetters } from 'vuex'
import ContactUs from '../ContactUs'
export default {
  components: {
    'app-contact-us': ContactUs
  },
  methods: {
    onCloseAlert() {
      this.$store.dispatch('contact/setingWasntSent')
    },
    onErrorAlert() {
      this.$store.dispatch('contact/setingClearError')
    }
  },
  computed: {
    ...mapGetters({
      sent: 'contact/successfullySent',
      msgError: 'contact/msgErrorRaised'
    })
  },
}
</script>
