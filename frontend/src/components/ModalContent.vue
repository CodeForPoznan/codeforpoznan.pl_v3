<template>
  <v-card>
    <v-card-title class="container-title unified-padding">
      <h1>{{ selectedProject.name }}</h1>
      <div>
        <v-btn class="hidden-xs-only" rounded icon large @click="onClick()">
          <v-icon size="3.5rem" color="white">close</v-icon>
        </v-btn>
      </div>
    </v-card-title>
    <v-card-actions class="buttons-list unified-padding">
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
      <p class="text-center">{{ selectedProject.description }}</p>
    </v-card-text>
    <div v-show="countPartners >> 0">
      <v-card-title class="container-subtitle unified-padding">
        <h2 v-if="countPartners === 1">
          Partner projektu
        </h2>
        <h2 v-else>Partnerzy projektu</h2>
      </v-card-title>
      <v-card-actions class="buttons-list unified-padding">
        <v-row
          class="partner-list"
          v-for="partners in selectedProject.partner"
          :key="partners.name"
        >
          <v-col class="partner-item" cols="12" sm="4">
            {{ partners.name }}
          </v-col>
          <v-col class="partner-item" cols="12" sm="3">
            <v-btn class="buttons-chips" text :href="partners.link" rounded>
              <span class="buttons-text">Poznaj</span>
              <v-icon>fas fa-hands-helping</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
    </div>
    <div v-show="countTech >> 0">
      <v-card-title class="container-subtitle unified-padding">
        <h2>Wykorzystane technologie</h2>
      </v-card-title>
      <v-card-actions class="buttons-list unified-padding">
        <v-btn
          v-for="(item, index) in selectedProject.stack"
          :key="index"
          :href="item.documentation"
          class="buttons-chips"
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
      class="buttons-close hidden-sm-and-up"
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

h1 {
  font-family: $font-header;
  font-size: 2.5rem;
  color: $white;
  word-break: break-word;
  margin-right: auto;
  @media only screen and (max-width: $phone) {
    font-size: 2rem;
    text-align: center;
    margin-right: 0;
  }
}

h2 {
  font-family: $font-content;
  font-size: 1.5rem;
  color: black;
  font-weight: bold;
  word-break: break-word;
  @media only screen and (max-width: $phone) {
    text-align: center;
  }
}

.buttons-close {
  background-color: $blue !important;
}

.buttons-list {
  display: flex;
  flex-wrap: wrap;
  @media only screen and (max-width: $phone) {
    justify-content: center;
  }
}

.buttons-chips {
  background-color: $blue;
  color: $white;
  margin: 0.2rem;
}

.buttons-text {
  margin: 0.5rem;
}

.container-title {
  background: $blue;
  min-height: 5rem;
  @media only screen and (max-width: $phone) {
    display: flex;
    justify-content: center;
  }
}

.container-subtitle {
  @media only screen and (max-width: $phone) {
    display: flex;
    justify-content: center;
  }
}

.partner-list {
  display: flex;
  align-items: center;
}

.partner-item {
  display: flex;
  justify-content: center;
  text-align: center;
  @media only screen and (max-width: $phone) {
    padding: 2% 20%;
  }
}

.unified-padding {
  padding: 0.5rem 1.5rem !important;
}
</style>
