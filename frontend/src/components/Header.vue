<template>
  <div>
    <v-app-bar class="navbar-custom" dark clipped-right color="#2C3E50">
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
        <template v-for="item in items">
          <v-tab align-right @click="$vuetify.goTo(item.id)" :key="item.id">{{
            item.name
          }}</v-tab>
        </template>
      </v-tabs>
    </v-app-bar>
    <v-list class="navbar-custom hidden-md-and-up" dark>
      <v-tabs background-color="transparent" vertical>
        <template v-for="item in items">
          <v-tab
            @click="$vuetify.goTo(item.id)"
            class="tab-custom"
            :key="item.id"
            >{{ item.name }}</v-tab
          >
        </template>
      </v-tabs>
    </v-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { name: 'O nas', id: '#about' },
        { name: 'Nasze projekty', id: '#projects' },
        { name: 'Dołącz do nas', id: '#join' },
        { name: 'Kontakt', id: '#contact' }
      ],
      image: require('@/assets/images/logo-white.svg')
    };
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';
.navbar-custom {
  font-family: $font-header;
  color: #ffffff !important;
}
.tab-custom {
  justify-content: left;
}
</style>
