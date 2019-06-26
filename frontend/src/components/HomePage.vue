<template>
<<<<<<< HEAD
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
      <app-contact-us/>
      <app-join-us/>
      <page-footer/>
    </v-app>
  </div>
=======
    <div>
        <v-app>
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
            <app-about-us />
            <app-contact-us />
            <social-media />
            <page-footer />
        </v-app>
    </div>
>>>>>>> bc9241dca2f89b4e1e5094782b010ac911c17930
</template>

<script>
import { mapGetters } from 'vuex';
import ContactUs from './ContactUs.vue';
import AboutUs from './AboutUs.vue';
import SocialMedia from './SocialMedia.vue';
import PageFooter from './PageFooter.vue';
import JoinUs from './JoinUs.vue';
export default {
<<<<<<< HEAD
  components: {
    'app-contact-us': ContactUs,
    'app-about-us': AboutUs,
    'app-join-us': JoinUs,
    'page-footer': PageFooter
  },
  methods: {
    onCloseAlert() {
      this.$store.dispatch('contact/setingWasntSent')
=======
    components: {
        'app-contact-us': ContactUs,
        'app-about-us': AboutUs,
        'social-media': SocialMedia,
        'page-footer': PageFooter
>>>>>>> bc9241dca2f89b4e1e5094782b010ac911c17930
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
@import './../main.scss';
.v-messages__message {
    padding: 2px;
}
</style>
