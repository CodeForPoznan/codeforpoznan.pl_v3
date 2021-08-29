<template>
  <div>
    <v-app-bar class="navbar-custom" dark clipped-right color="#2C3E50">
      <v-toolbar-title>
        <a href="https://codeforpoznan.pl/">
          <v-img
            :src="cfpLogo"
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
      <v-app-bar-nav-icon
        @click="drawer = !drawer"
        class="hidden-md-and-up"
      ></v-app-bar-nav-icon>
      <v-tabs background-color="transparent" right class="hidden-sm-and-down">
        <v-tab align-right @click="onLogout">Logout</v-tab>
      </v-tabs>
    </v-app-bar>
    <v-list class="navbar-custom hidden-md-and-up" dark>
      <v-expand-transition>
        <v-tabs
          width="100%"
          v-if="drawer"
          background-color="transparent"
          vertical
        >
          <div class="mobile-tab-items">
            <v-tab @click="onLogout" class="tab-custom">Logout</v-tab>
          </div>
        </v-tabs>
      </v-expand-transition>
    </v-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cfpLogo: require('@/assets/images/logo-white.svg'),
      drawer: false
    };
  },
  methods: {
    async onLogout() {
      await this.$store.dispatch('auth/logout');
      this.$router.push('/');
    }
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';
.navbar-custom {
  font-family: $font-header;
  padding: 0;
}
.tab-custom {
  justify-content: left;
  max-width: none;
}
.mobile-tab-items {
  width: 100vw;
}
</style>
