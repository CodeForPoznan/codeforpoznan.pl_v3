<template>
  <div>
    <v-app-bar class="navbar-custom" dark clipped-right>
      <v-toolbar-title>
        <a href="https://codeforpoznan.pl/">
          <v-img
            :src="image"
            contain
            max-height="20"
            aspect-ratio="1.7"
            max-width="500"
            min-width="350"
            position="left"
          ></v-img>
        </a>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-tabs
        background-color="transparent"
        right
        class="hidden-sm-and-down"
        mobile-break-point="768px"
      >
        <v-tab align-right @click="onLogout">Logout</v-tab>
      </v-tabs>
    </v-app-bar>
    <v-list class="navbar-custom hidden-md-and-up" dark>
      <v-tabs background-color="transparent" vertical>
        <v-tab @click="onLogout" class="tab-custom">Logout</v-tab>
      </v-tabs>
    </v-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      image: require('@/assets/images/logo-white.svg')
    };
  },
  methods: {
    onLogout() {
      this.$store.dispatch('auth/logout').then(() => {
        this.$router.push('/');
      });
    }
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';
.navbar-custom {
  font-family: $font-header;
  background-color: $blue-media-hr !important;
  color: #ffffff !important;
}
.tab-custom {
  justify-content: left;
}
</style>
