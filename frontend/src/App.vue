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
  created() {
    document.title = 'Code for Poznań';
  }
};
</script>
