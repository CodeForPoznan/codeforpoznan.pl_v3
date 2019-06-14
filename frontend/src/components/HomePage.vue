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
      <app-about-us/>
      <div>
        <app-our-projects/>
      </div>
      <app-contact-us/>
    </v-app>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import ContactUs from './ContactUs.vue'
import AboutUs from './AboutUs.vue'
import OurProjects from './OurProjects.vue'
export default {
  components: {
    'app-contact-us': ContactUs,
    'app-about-us': AboutUs,
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

<style lang="scss" scoped>
@import "./../main.scss";
.v-messages__message {
    padding: 2px;
  }
</style>

