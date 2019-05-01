<template>
  <div>
    <v-app>
      <v-container fluid id="logo-page">
        <v-layout align-center justify-center fill-height>
          <v-img
            :src="image"
            max-height="500px"
            contain
          >
          </v-img>
        </v-layout>
      </v-container>
    </v-app>
  </div>
</template>

<script>
export default{
  data () {
    return {
      image: require('@/assets/images/logo_codeforpoznan.svg'),
    }
  }
}
</script>

<style>
  #logo-page {
    background: #07a3e5;
  }
</style>
