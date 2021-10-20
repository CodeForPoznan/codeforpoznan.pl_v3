<template>
  <div>
    <v-app>
      <router-view></router-view>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'app',
  mounted() {
    if (localStorage.fontSize) {
      document.getElementsByTagName('html')[0].style.fontSize =
        localStorage.fontSize;
    }
  }
};
</script>
