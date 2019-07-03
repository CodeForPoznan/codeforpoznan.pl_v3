<template>
  <div>
    <v-app>
      <div>
        <v-alert
          :value="sent"
          dismissible
          @click="onCloseAlert"
          type="success"
          transition="slide-y-transition">
          Twoja wiadomość została wysłana
        </v-alert>
        <v-alert
          :value="msgError"
          dismissible
          @click="onErrorAlert"
          type="error"
          transition="slide-y-transition">
          Błąd w trakcie wysyłania wiadomości
        </v-alert>
      </div>
      <app-contact-us/>
      <app-header></app-header>
    </v-app>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import ContactUs from './ContactUs.vue'
import Header from './Header.vue'
export default {
  components: {
    'app-contact-us': ContactUs,
    'app-header': Header
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
  }
}
</script>

<style lang="css">

</style>

