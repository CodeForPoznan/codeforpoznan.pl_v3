<template>
  <div>
    <app-header />
    <v-main>
      <app-about-us />
      <our-projects />
      <app-join-us />
      <div>
        <v-alert
          :value="sent"
          dismissible
          @click="onCloseAlert"
          type="success"
          transition="slide-y-transition"
        >
          Twoja wiadomość została wysłana
        </v-alert>
        <v-alert
          :value="msgError"
          dismissible
          @click="onErrorAlert"
          type="error"
          transition="slide-y-transition"
        >
          Błąd w trakcie wysyłania wiadomości
        </v-alert>
      </div>
      <app-contact-us />
      <social-media />
    </v-main>
    <page-footer />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Header from './Header/Header.vue';
import ContactUs from './ContactUs/ContactUs.vue';
import AboutUs from './AboutUs/AboutUs.vue';
import SocialMedia from './SocialMedia/SocialMedia.vue';
import PageFooter from './PageFooter/PageFooter.vue';
import OurProjects from './OurProjects/OurProjects.vue';
import JoinUs from './JoinUs/JoinUs.vue';
export default {
  components: {
    'app-header': Header,
    'app-contact-us': ContactUs,
    'app-about-us': AboutUs,
    'social-media': SocialMedia,
    'our-projects': OurProjects,
    'app-join-us': JoinUs,
    'page-footer': PageFooter
  },
  methods: {
    onCloseAlert() {
      this.$store.dispatch('contact/setingWasntSent');
    },
    onErrorAlert() {
      this.$store.dispatch('contact/setingClearError');
    }
  },
  computed: {
    ...mapGetters({
      sent: 'contact/successfullySent',
      msgError: 'contact/msgErrorRaised'
    })
  }
};
</script>

<style lang="scss" scoped>
@import '../../main.scss';
.v-messages__message {
  padding: 2px;
}
</style>
