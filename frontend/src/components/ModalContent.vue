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
      <div class="buttons-list">
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
      </div>
    </v-card-actions>
    <div class="text-list">
      <v-row>
        <pre class="modal-subtitle">Partner projektu: </pre>
        <p class="modal-subtitle">{{ selectedProject.partner }}</p>
      </v-row>
    </div>
    <div class="text-list">
      <v-row>
        <p class="content-black">{{ selectedProject.description }}</p>
      </v-row>
    </div>
    <div class="text-list">
      <v-row>
        <p class="modal-subtitle">Wykorzystane technologie:</p>
      </v-row>
    </div>
    <v-card-actions>
      <div class="buttons-list">
        <v-row>
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
      </div>
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

.buttons-list {
  margin: 0.5rem 2rem;
}

.text-list {
  margin: 0.25rem 3rem;
}

.buttons {
  margin: 1rem 0.5rem 1rem 0;
}

.buttons--text {
  display: flex;
  align-content: center;
  margin: 0.5rem;
}

.content-black {
  color: black;
  text-align: justify;
}

.modal-title {
  display: flex;
  align-content: center;
  font-family: $font-header;
  font-size: 3rem;
  padding: 2rem 0;
  color: $white;
  margin: 0.5rem 0 0 1.2rem;
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

.title-header {
  background: $blue;
}
</style>
