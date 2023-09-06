<template>
  <div>
    <v-app-bar class="navbar-custom" app dark color="#2C3E50">
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
        v-model="activeTabIndex"
      >
        <v-tab
          v-for="item in items"
          :key="item.id"
          align-right
          theme="dark"
          :data-section-selector="item.id"
          class="scrollactive-item tab-custom"
          @click.prevent="scrollTo(item.id)"
          >{{ item.name }}
        </v-tab>
      </v-tabs>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      location="top"
      temporary
      rail="true"
      rail-width="190"
      @click="drawer = false"
    >
      <v-list class="navbar-custom hidden-md-and-up" dark>
        <v-list-item
          v-for="item in items"
          :key="item.id"
          class="mobile-tab-custom"
          @click.prevent="scrollTo(item.id)"
        >
          {{ item.name }}
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
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
        { name: 'Kontakt', id: '#contact' },
      ],
      cfpLogo: require('@/assets/images/logo-white.svg'),
      drawer: false,
      activeTabIndex: null,
    };
  },
  methods: {
    onActiveTabChanged(_, currentItem) {
      if (currentItem) {
        const activeItemIndex = this.items.findIndex(
          (item) => item.id === currentItem.dataset.sectionSelector
        );

        this.activeTabIndex = activeItemIndex;
      }
    },
    scrollTo(element_id) {
      const el = document.querySelector(element_id);

      el.scrollIntoView({ behavior: 'smooth' });
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
