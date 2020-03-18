<template>
  <v-container fluid class="white-container" id="projects">
    <v-row>
      <v-col>
        <v-card flat color="transparent">
          <v-card-text class="title">
            <p class="blue-title">NASZE PROJEKTY</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row wrap>
      <v-col
        class="items"
        v-for="(project, index) in projects"
        :key="index"
        cols="12"
        xs="12"
        md="6"
        lg="4"
        xl="3"
      >
        <v-item-group>
          <v-hover v-slot="{ hover }">
            <v-card @click.stop="clickImage(project)">
              <v-img :src="project.imageAdress" aspect-ratio="1.9" />
              <v-card-title class="card">
                {{ project.name }}
              </v-card-title>
              <v-expand-transition>
                <div v-if="hover" class="card--reveal">
                  <v-img class="card--hover" :src="hoveredImg" />
                </div>
              </v-expand-transition>
            </v-card>
          </v-hover>
        </v-item-group>
      </v-col>
    </v-row>
    <v-dialog v-model="dialog" max-width="50rem">
      <app-modal-content :selectedProject="selectedProject" />
    </v-dialog>
  </v-container>
</template>

<script>
import ModalContent from './ModalContent.vue';
import projects from '../assets/projects';
export default {
  components: {
    'app-modal-content': ModalContent
  },
  data() {
    return {
      dialog: false,
      hoveredImg: require('@/assets/images/magnifying_glass.svg'),
      projects: projects,
      selectedProject: []
    };
  },
  methods: {
    clickImage(project) {
      this.dialog = true;
      this.selectedProject = project;
    }
  },
  mounted() {
    this.$root.$on('close', () => {
      this.dialog = false;
    });
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

.card {
  font-family: $font-header;
  font-size: 1.5rem;
  justify-content: center;
}

.card--hover {
  max-width: 50%;
}

.card--reveal {
  background: $blue;
  bottom: 0;
  color: $white;
  display: flex;
  justify-content: center;
  opacity: 0.9;
  position: absolute;
  width: 100%;
  height: 100%;
}

.items {
  padding: 10px;
}
</style>
