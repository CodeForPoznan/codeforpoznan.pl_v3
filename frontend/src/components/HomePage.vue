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
      </div>
      <app-contact-us/>
    </v-app>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import ContactUs from './ContactUs.vue'

export default {
  components: {
    'app-contact-us': ContactUs
  },
  methods: {
    onCloseAlert() {
      this.$store.dispatch('contact/setingWasntSent')
    }
  },
  computed: {
    ...mapGetters({
      sent: 'contact/successfullySent'
    })
  },
}
</script>

<style lang="css">
</style>
