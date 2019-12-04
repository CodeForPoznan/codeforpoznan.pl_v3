<template>
  <v-card>
    <v-card-title id="title-header">
      <v-row>
        <p id="modal-title">{{ selectedProject.name }}</p>
        <v-card-actions>
          <v-btn
            class="mr-2"
            absolute
            fab
            rounded
            icon
            large
            right
            @click="onClick()"
          >
            <v-icon size="3.5rem" color="white">close</v-icon>
          </v-btn>
        </v-card-actions>
      </v-row>
    </v-card-title>
    <v-card-text>
      <v-card-actions>
        <v-btn text rounded :href="selectedProject.licensePage" target="_blank">
          <v-icon>far fa-copyright</v-icon>
          <p class="buttons">Licencja {{ selectedProject.licenseName }}</p>
        </v-btn>
        <v-btn text rounded :href="selectedProject.websiteLink" target="_blank">
          <v-icon>language</v-icon>
          <p class="buttons">Strona WWW</p>
        </v-btn>
        <v-btn text rounded :href="selectedProject.githubLink" target="_blank">
          <v-icon>fab fa-github</v-icon>
          <p class="buttons">Repozytorium</p>
        </v-btn>
      </v-card-actions>
    </v-card-text>
    <v-card-text>
      <v-row class="ml-3 mr-3">
        <p class="modal-subtitle">
          Partner projektu:
        </p>
        <v-btn text rounded :href="selectedProject.partnerPage" target="_blank">
          <a class="modal-subtitle">{{ selectedProject.partner }}</a>
        </v-btn>
      </v-row>
      <v-row>
        <p class="content--black">{{ selectedProject.description }}</p>
      </v-row>
      <v-row class="ml-3 mr-3">
        <p class="modal-subtitle">Wykorzystane technologie:</p>
      </v-row>
      <v-row class="mr-1 ml-1">
        <v-btn
          class="stack-list ma-2"
          v-for="(item, index) in selectedProject.stack"
          :key="index"
          :href="item.documentation"
          target="_blank"
          rounded
        >
          {{ item.type }}: {{ item.name }} {{ item.version }}
        </v-btn>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ['selectedProject'],
  methods: {
    onClick() {
      this.$root.$emit('close');
    }
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

a {
  text-transform: none;
}

.buttons {
  display: flex;
  align-content: center;
  margin: 0.5rem;
}

#close-button {
  display: flex;
  color: $white;
  max-width: 3rem;
  margin: 1rem;
}

.content--black {
  color: black;
  text-align: justify;
  margin: 1rem 1.5rem;
}

#modal-title {
  display: flex;
  align-content: center;
  font-family: $font-header;
  font-size: 3rem;
  color: $white;
  margin: 0.5rem 0rem 0rem 2rem;
}

.modal-subtitle {
  color: black;
  display: flex;
  position: relative;
  align-content: center;
  font-family: $font-content;
  font-size: 1.5rem;
  line-height: 1.43;
  font-weight: bold;
}

.stack-list {
  background-color: $blue !important;
  color: $white;
}

#title-header {
  background: $blue;
  height: 7rem;
}
</style>
