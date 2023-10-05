<template>
  <div>
    <v-app-bar class="navbar-custom" dark app color="#2C3E50">
      <v-toolbar-title class="d-inline">
        <v-row>
          <v-col class="d-flex child-flex">
            <a href="https://codeforpoznan.pl/">
              <v-img
                :src="cfpLogo"
                max-height="22"
                aspect-ratio="1.5"
                max-width="500"
                min-width="250"
                inline
              ></v-img>
            </a>
          </v-col>
        </v-row>
      </v-toolbar-title>
      <v-app-bar-nav-icon
        variant="text"
        @click.stop="drawer = !drawer"
        class="hidden-md-and-up"
        color="white"
      ></v-app-bar-nav-icon>
      <v-tabs
        bg-color="#2C3E50"
        color="white"
        dark
        height="64"
        right
        class="hidden-sm-and-down"
      >
        <v-tab align-right theme="dark" class="tab-custom" @click="onLogout"
          >Logout</v-tab
        >
      </v-tabs>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      location="top"
      temporary
      :rail="true"
      rail-width="190"
      @click="drawer = false"
    >
      <v-list class="navbar-custom hidden-md-and-up" dark>
        <v-list-item class="mobile-tab-custom" @click.prevent="onLogout">
          Logout
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cfpLogo: require('@/assets/images/logo-white.svg'),
      drawer: false,
    };
  },
  methods: {
    async onLogout() {
      await this.$store.dispatch('auth/logout');
      this.$router.push('/');
    },
  },
};
</script>

<style lang="scss" scoped>
@import '../../../main.scss';
.navbar-custom {
  font-family: $font-header;
  padding: 0;
}
.tab-custom {
  color: hsla(0, 0%, 100%, 0.6);
}
.mobile-tab-custom {
  justify-content: left;
  max-width: none;
}
</style>
