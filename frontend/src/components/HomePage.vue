<template>
  <div>
    <v-app>
      <div>
        <app-our-projects/>
      </div>
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
    </v-app>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import ContactUs from './ContactUs.vue'
import OurProjects from './OurProjects'
export default {
  components: {
    'app-contact-us': ContactUs,
    'app-our-projects': OurProjects
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

<style lang="css">
</style>
