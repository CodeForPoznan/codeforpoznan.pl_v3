<template>
  <v-card>
    <v-card-title class="header-container">
      <h1>{{ selectedProject.name }}</h1>
      <v-spacer></v-spacer>
      <div>
        <v-btn class="hidden-xs-only" rounded icon large @click="onClick()">
          <v-icon size="3.5rem" color="white">close</v-icon>
        </v-btn>
      </div>
    </v-card-title>
    <v-card-actions class="icon-list">
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
    <v-card-text>
      <p>{{ selectedProject.description }}</p>
    </v-card-text>
    <div v-if="countPartners === 1 && selectedProject.partner.name === ''">
      <v-card-title>
        <div v-if="countPartners === 1">
          Partner projektu
        </div>
        <div v-else>Partnerzy projektu</div>
      </v-card-title>
      <v-card-actions class="icon-list" ma-0 pa-0>
        <div>
          <v-btn
            class="ma-0 buttons-text"
            v-for="(item, index) in selectedProject.partner"
            :key="index"
            :href="item.link"
            target="_blank"
            text
            rounded
          >
            <v-icon>fas fa-link</v-icon>
            <span class="buttons-text">{{ item.name }}</span>
          </v-btn>
        </div>
      </v-card-actions>
    </div>
    <v-card-title>Wykorzystane technologie</v-card-title>
    <v-card-actions>
      <div>
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
      </div>
    </v-card-actions>

    <!--    <div class="text-list">-->
    <!--      <v-row>-->
    <!--        <pre class="modal-subtitle">Partner projektu: </pre>-->
    <!--        <p class="modal-subtitle">{{ selectedProject.partner }}</p>-->
    <!--      </v-row>-->
    <!--    </div>-->
    <!--    <div class="text-list">-->
    <!--      <v-row>-->
    <!--        <p class="content-black">{{ selectedProject.description }}</p>-->
    <!--      </v-row>-->
    <!--    </div>-->
    <!--    <div class="text-list">-->
    <!--      <v-row>-->
    <!--        <p class="modal-subtitle">Wykorzystane technologie:</p>-->
    <!--      </v-row>-->
    <!--    </div>-->
    <!--    <v-card-actions>-->
    <!--      <div class="buttons-list">-->
    <!--        <v-row>-->
    <!--          <v-btn-->
    <!--            v-for="(item, index) in selectedProject.stack"-->
    <!--            :key="index"-->
    <!--            :href="item.documentation"-->
    <!--            class="stack-list"-->
    <!--            target="_blank"-->
    <!--            text-->
    <!--            rounded-->
    <!--          >-->
    <!--            {{ item.type }}: {{ item.name }} {{ item.version }}-->
    <!--          </v-btn>-->
    <!--        </v-row>-->
    <!--      </div>-->
    <!--    </v-card-actions>-->
    <v-btn
      fixed
      bottom
      right
      rounded
      class="hidden-sm-and-up"
      fab
      color="#0CAEE7"
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
      partners: '',
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
    countPartnerNames() {
      return this.selectedProject.partner.name.length;
    }
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

a {
  text-transform: none;
}

.header-container {
  background: $blue;
  min-height: 5rem;
}

h1 {
  font-family: $font-header;
  font-size: 2rem;
  color: $white;
  word-break: break-word;
  @media only screen and (max-width: $phone) {
    font-size: 1.5rem;
  }
}

.buttons-text {
  margin: 0.4rem;
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: normal;
}

.icon-list {
  display: flex;
  flex-wrap: wrap;
}

//

.title-row {
  display: flex;
  flex-wrap: wrap-reverse;
}

.buttons-list {
  margin: 0.5rem 2rem;
}

.text-list {
  margin: 0.25rem 3rem;
}

.content-black {
  color: black;
  text-align: justify;
}

.modal-subtitle {
  color: black;
  font-family: $font-content;
  font-size: 1.5rem;
  font-weight: bold;
  line-height: 1.43;
  margin: 0.5rem 0rem;
}

.stack-list {
  background-color: $blue;
  color: $white;
  margin: 0.5rem 0.5rem 0.5rem 0.5rem;
}

.text-row {
  padding: 1px;
}

.kurwa {
  color: $blue;
}
</style>
