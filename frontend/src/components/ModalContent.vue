<template>
  <v-card class="card-container">
    <v-card-title class="header-container unified-padding">
      <h1>{{ selectedProject.name }}</h1>
      <v-spacer></v-spacer>
      <div>
        <v-btn class="hidden-xs-only" rounded icon large @click="onClick()">
          <v-icon size="3.5rem" color="white">close</v-icon>
        </v-btn>
      </div>
    </v-card-title>
    <v-card-actions class="icon-list unified-padding">
      <div v-show="selectedProject.licensePage !== ''">
        <v-btn text rounded :href="selectedProject.licensePage" target="_blank">
          <v-icon>far fa-copyright</v-icon>
          <span class="buttons-text"
            >Licencja {{ selectedProject.licenseName }}</span
          >
        </v-btn>
      </div>
      <div v-show="selectedProject.githubLink !== ''">
        <v-btn text rounded :href="selectedProject.githubLink" target="_blank">
          <v-icon>fab fa-github</v-icon>
          <span class="buttons-text">Repozytorium</span>
        </v-btn>
      </div>
      <div v-show="selectedProject.websiteLink !== ''">
        <v-btn text rounded :href="selectedProject.websiteLink" target="_blank">
          <v-icon>language</v-icon>
          <span class="buttons-text">Strona projektu</span>
        </v-btn>
      </div>
    </v-card-actions>
    <v-card-text class="unified-padding">
      <p>{{ selectedProject.description }}</p>
    </v-card-text>
    <div v-show="countPartners >> 0">
      <v-card-title class="unified-padding">
        <h2 v-if="countPartners === 1">
          Partner projektu
        </h2>
        <h2 v-else>Partnerzy projektu</h2>
      </v-card-title>
      <v-card-actions class="icon-list unified-padding">
        <v-btn
          class="ma-0 buttons-text"
          v-for="(item, index) in selectedProject.partner"
          :key="index"
          :href="item.link"
          target="_blank"
          text
          rounded
        >
          <v-icon>fas fa-hands-helping</v-icon>
          <span class="buttons-text">{{ item.name }}</span>
        </v-btn>
      </v-card-actions>
    </div>
    <div v-show="countTech >> 0">
      <v-card-title class="unified-padding">
        <h2>Wykorzystane technologie</h2>
      </v-card-title>
      <v-card-actions class="icon-list unified-padding">
        <v-btn
          v-for="(item, index) in selectedProject.stack"
          :key="index"
          :href="item.documentation"
          class="stack-list"
          target="_blank"
          text
          rounded
        >
          {{ item.type }}: {{ item.name }} {{ item.version }}
        </v-btn>
      </v-card-actions>
    </div>
    <v-btn
      fixed
      bottom
      right
      rounded
      class="close-button hidden-sm-and-up"
      fab
      @click="onClick()"
    >
      <v-icon size="3.5rem" color="white">close</v-icon>
    </v-btn>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      partnerSection: null,
      multiplePartners: null
    };
  },
  props: ['selectedProject'],
  methods: {
    onClick() {
      this.$root.$emit('close');
    }
  },
  computed: {
    countPartners() {
      return this.selectedProject.partner.length;
    },
    countTech() {
      return this.selectedProject.stack.length;
    }
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

a {
  text-transform: none;
}

.unified-padding {
  padding: 0.5rem 1.5rem !important;
}

.header-container {
  background: $blue;
  min-height: 5rem;
}

h1 {
  font-family: $font-header;
  font-size: 2.5rem;
  color: $white;
  word-break: break-word;
  @media only screen and (max-width: $phone) {
    font-size: 2rem;
  }
}

h2 {
  font-family: $font-content;
  font-size: 1.5rem;
  color: black;
  font-weight: bold;
}

.buttons-text {
  margin: 0.4rem;
}

.icon-list {
  display: flex;
  flex-wrap: wrap;
}

.close-button {
  background-color: $blue !important;
}

.stack-list {
  background-color: $blue;
  color: $white;
  margin: 0.5rem 0.5rem 0.5rem 0.5rem;
}
</style>
