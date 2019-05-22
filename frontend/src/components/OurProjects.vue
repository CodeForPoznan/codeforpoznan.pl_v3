<template>
  <div>
    <v-content>
      <ul>
        <li v-for="project in projects">{{project.name}}</li>
      </ul>
    </v-content>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        projects: [
          {name: 'Volontulo'},
          {name: 'Wysadź ulicę'},
          {name: 'Bank Empatii'},
          {name: 'Alinka'},
          {name: 'Polska Akcja Humanitarna'}
        ]
      }
    }
  }
</script>

<style scoped>

</style>