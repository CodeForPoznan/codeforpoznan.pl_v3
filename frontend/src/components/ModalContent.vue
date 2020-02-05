<template>
  <v-card>
    <v-card-title class="title-header">
      <v-row>
        <p class="modal-title">{{ selectedProject.name }}</p>
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
    <v-card-actions>
      <v-row>
        <v-btn
          class="buttons"
          text
          rounded
          large
          :href="selectedProject.licensePage"
          target="_blank"
        >
          <v-icon>far fa-copyright</v-icon>
          <p class="buttons--text">
            Licencja {{ selectedProject.licenseName }}
          </p>
        </v-btn>
        <v-btn
          class="buttons"
          text
          rounded
          large
          :href="selectedProject.githubLink"
          target="_blank"
        >
          <v-icon>fab fa-github</v-icon>
          <p class="buttons--text">Repozytorium</p>
        </v-btn>
        <v-btn
          class="buttons"
          text
          rounded
          large
          :href="selectedProject.websiteLink"
          target="_blank"
        >
          <v-icon>language</v-icon>
          <p class="buttons--text">Strona projektu</p>
        </v-btn>
        <v-btn
          class="buttons"
          text
          rounded
          large
          :href="selectedProject.partnerPage"
          target="_blank"
        >
          <v-icon>fas fa-handshake</v-icon>
          <p class="buttons--text">Strona partnera</p>
        </v-btn>
      </v-row>
    </v-card-actions>
    <v-card-text>
      <v-row>
        <div>
          <p class="modal-subtitle">Partner projektu:</p>
          <p class="modal-subtitle">{{ selectedProject.partner }}</p>
        </div>
      </v-row>
      <v-row>
        <p class="content-black">{{ selectedProject.description }}</p>
      </v-row>
      <v-row>
        <p class="modal-subtitle">Wykorzystane technologie:</p>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-row class="mr-1 ml-1">
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
      </v-row>
    </v-card-actions>
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
  margin: 0rem 1rem 1rem 2rem;
}

.buttons--text {
  display: flex;
  align-content: center;
  margin: 0.5rem;
}

.button-row {
  display: flex;
  padding: 8px 36px;
  align-items: flex-start;
}

.content-black {
  color: black;
  text-align: justify;
  margin: 1rem 1.5rem;
}

.modal-title {
  display: flex;
  align-content: center;
  font-family: $font-header;
  font-size: 3rem;
  padding: 2rem 0;
  color: $white;
  margin: 0.5rem 0 0 2rem;
}

.modal-subtitle {
  align-self: auto;
  justify-content: space-around;
  color: black;
  display: flex;
  font-family: $font-content;
  font-size: 1.5rem;
  font-weight: bold;
  line-height: 1.43;
  position: relative;
  padding-left: 2rem;
}

.stack-list {
  background-color: $blue;
  color: $white;
  margin: 4px;
}

.text-row {
  padding: 1px;
}

.title-header {
  background: $blue;
}
</style>
