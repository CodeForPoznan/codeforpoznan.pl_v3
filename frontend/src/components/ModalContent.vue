<template>
  <v-card class="modal">
    <v-card-title class="modal__title">
      <h1>{{ selectedProject.name }}</h1>
      <div>
        <v-btn class="hidden-xs-only" rounded icon large @click="onClick()">
          <v-icon size="3.5rem" color="white">close</v-icon>
        </v-btn>
      </div>
    </v-card-title>
    <v-card-actions class="modal__buttons">
      <div v-show="selectedProject.licensePage !== ''">
        <v-btn text rounded :href="selectedProject.licensePage" target="_blank">
          <v-icon>far fa-copyright</v-icon>
          <span class="modal__button-text"
            >Licencja {{ selectedProject.licenseName }}</span
          >
        </v-btn>
      </div>
      <div v-show="selectedProject.githubLink !== ''">
        <v-btn text rounded :href="selectedProject.githubLink" target="_blank">
          <v-icon>fab fa-github</v-icon>
          <span class="modal__button-text">Repozytorium</span>
        </v-btn>
      </div>
      <div v-show="selectedProject.websiteLink !== ''">
        <v-btn text rounded :href="selectedProject.websiteLink" target="_blank">
          <v-icon>language</v-icon>
          <span class="modal__button-text">Strona projektu</span>
        </v-btn>
      </div>
    </v-card-actions>
    <v-card-text class="modal__description">
      <p class="text-center">{{ selectedProject.description }}</p>
    </v-card-text>
    <div v-show="countPartners >> 0">
      <v-card-title class="modal__title">
        <h2 v-if="countPartners === 1">
          Partner projektu
        </h2>
        <h2 v-else>Partnerzy projektu</h2>
      </v-card-title>
      <v-card-actions class="modal__buttons">
        <v-row
          class="modal__partners"
          v-for="partners in selectedProject.partner"
          :key="partners.name"
        >
          <v-col class="modal__partner" cols="12" sm="5">
            {{ partners.name }}
          </v-col>
          <v-col class="modal__partner" cols="12" sm="4">
            <v-btn
              class="modal__button"
              :href="partners.link"
              target="_blank"
              rounded
              text
            >
              <span class="modal__button-text">Poznaj</span>
              <v-icon>fas fa-hands-helping</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
    </div>
    <div v-show="countTech >> 0">
      <v-card-title class="modal__title">
        <h2>Wykorzystane technologie</h2>
      </v-card-title>
      <v-card-actions class="modal__buttons">
        <v-btn
          v-for="(item, index) in selectedProject.stack"
          :key="index"
          :href="item.documentation"
          class="modal__button"
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
      class="modal__button-close hidden-sm-and-up"
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

h1,
h2 {
  font-size: 1.5rem;
  color: black;
  font-family: $font-header;
  word-break: break-word;
  @media only screen and (max-width: $phone) {
    text-align: center;
  }
}

h1 {
  font-size: 2.5rem;
  color: $white;
  @media only screen and (max-width: $phone) {
    font-size: 2rem;
  }
}

.modal__buttons,
.modal__description,
.modal__title {
  padding: 0.5rem 1.5rem;
}

.modal > .modal__title {
  background: $blue;
}

.modal__buttons {
  display: flex;
  flex-wrap: wrap;
  @media only screen and (max-width: $phone) {
    justify-content: center;
  }
}

.modal__button {
  background-color: $blue;
  color: $white;
  margin: 0.2rem;
}

.modal__button-close {
  background-color: $blue !important;
}

.modal__button-text {
  margin: 0.5rem;
}

.modal__partners {
  display: flex;
  align-items: center;
}

.modal__partner {
  @media only screen and (max-width: $phone) {
    padding: 2% 10%;
    text-align: center;
  }
}

.modal__title {
  @media only screen and (max-width: $phone) {
    display: flex;
    justify-content: center;
  }
}
</style>
