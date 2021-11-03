<template>
  <div>
    <v-app>
      <router-view></router-view>
    </v-app>
  </div>
</template>

<script>
import { adjustFontSize } from './helpers/font-size.js';
export default {
  name: 'app',
  mounted() {
    this.adjustFontSize();
    window.addEventListener('resize', this.adjustFontSize);
  },
  unmounted() {
    window.removeEventListener('resize', this.adjustFontSize);
  },
  methods: {
    adjustFontSize
  }
};
</script>
