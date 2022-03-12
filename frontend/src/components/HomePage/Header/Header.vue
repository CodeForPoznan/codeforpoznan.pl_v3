<template>
  <div>
    <v-app-bar class="navbar-custom" app dark color="#2C3E50">
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
      <Scrollactive :offset="64" @itemchanged="onActiveTabChanged">
        <v-tabs
          background-color="transparent"
          height="64"
          right
          class="hidden-sm-and-down"
          v-model="activeTabIndex"
        >
          <v-tab
            v-for="item in items"
            :key="item.id"
            align-right
            :data-section-selector="item.id"
            class="scrollactive-item"
            >{{ item.name }}
          </v-tab>
        </v-tabs>
      </Scrollactive>
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
            <template v-for="item in items">
              <v-tab
                @click="$vuetify.goTo(item.id)"
                class="tab-custom"
                :key="item.id"
                >{{ item.name }}</v-tab
              >
            </template>
          </div>
        </v-tabs>
      </v-expand-transition>
    </v-list>
  </div>
</template>

<script>
import Scrollactive from 'vue-scrollactive/src/scrollactive.vue';

export default {
  data() {
    return {
      items: [
        { name: 'O nas', id: '#about' },
        { name: 'Nasze projekty', id: '#projects' },
        { name: 'Dołącz do nas', id: '#join' },
        { name: 'Kontakt', id: '#contact' }
      ],
      cfpLogo: require('@/assets/images/logo-white.svg'),
      drawer: false,
      activeTabIndex: null
    };
  },
  components: {
    Scrollactive
  },
  methods: {
    onActiveTabChanged(_, currentItem) {
      if (currentItem) {
        const activeItemIndex = this.items.findIndex(
          item => item.id === currentItem.dataset.sectionSelector
        );

        this.activeTabIndex = activeItemIndex;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
@import '../../../main.scss';
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
