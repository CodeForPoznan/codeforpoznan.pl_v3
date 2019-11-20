<template>
  <v-card>
    <v-row id="header">
      <v-col d-flex justify-content>
        <p id="title">{{ selectedProject.projectName }}</p>
      </v-col>
      <v-col id="close">
        <v-card-actions>
          <v-btn absolute fab rounded icon large right @click="onClick()">
            <v-icon size="3.5rem" color="white">close</v-icon>
          </v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
    <v-row class="pa-2">
      <v-card-actions>
        <v-btn flat round :href="selectedProject.licensePage" target="_blank">
          <v-icon>far fa-copyright</v-icon>
          <p class="buttons">Licencja {{ selectedProject.licenseName }}</p>
        </v-btn>
        <v-btn flat round :href="selectedProject.websiteLink" target="_blank">
          <v-icon>language</v-icon>
          <p class="buttons">Strona WWW</p>
        </v-btn>
        <v-btn flat round :href="selectedProject.githubLink" target="_blank">
          <v-icon>fab fa-github</v-icon>
          <p class="buttons">Repozytorium</p>
        </v-btn>
      </v-card-actions>
    </v-row>
    <v-card-text class="content">
      <v-layout class="pa-2">
        <p class="partner font-weight-bold align-center">
          Partner projektu:
        </p>
        <v-btn round flat :href="selectedProject.partnerPage" target="_blank">
          <p class="partner">{{ selectedProject.partner }}</p>
        </v-btn>
      </v-layout>
      <v-layout class="pa-2">
        {{ selectedProject.description }}
      </v-layout>
      <v-layout class="pa-2">
        <p class="partner font-weight-bold align-center">Stack:</p>
        <v-btn
          v-for="(item, index) in selectedProject.stack"
          :key="index"
          :href="item.documentation"
          target="_blank"
          round
          id="stack-list"
        >
          {{ item.type }}: {{ item.name }} {{ item.version }}
        </v-btn>
      </v-layout>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      copyleftIcon: require('@/assets/images/copyleft.svg')
    };
  },
  props: ['selectedProject', 'dialog'],
  methods: {
    onClick() {
      this.$root.$emit('close');
    }
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

.buttons {
  display: flex;
  align-content: center;
  margin: 0.5rem;
}

#close {
  display: flex;
  color: $white;
  max-width: 3rem;
  margin: 1rem;
}

#header {
  background: $blue;
  height: 7rem;
}

#title {
  display: flex;
  align-content: center;
  font-family: $font-header;
  font-size: 3rem;
  color: $white;
  margin: 0rem 0rem 0rem 2rem;
}

.content {
  font-family: $font-content;
  font-size: 1.5rem;
  padding: 0rem 1rem 1rem 1rem;
  line-height: 1.43;
}

.partner {
  display: flex;
  position: relative;
  align-content: center;
  font-family: $font-content;
  font-size: 1.5rem;
  line-height: 1.43;
  margin: 0.1rem;
}

#stack-list {
  background-color: $blue;
  color: $white;
}
</style>
