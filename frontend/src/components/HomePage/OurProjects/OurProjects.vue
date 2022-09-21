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
        v-for="project in orderedProjects"
        :key="project.id"
        cols="12"
        xs="12"
        md="6"
        lg="4"
        xl="3"
      >
        <v-item-group>
          <v-hover v-slot="{ hover }">
            <v-card @click.stop="clickImage(project)">
              <v-img :src="project.imageAdress" aspect-ratio="1.9">
                <div :class="'card_badge--' + project.badge" />
              </v-img>
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
import ModalContent from './ModalContent/ModalContent.vue';
import projects from '../../../assets/projects';
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
  computed: {
    orderedProjects: function() {
      return _.orderBy(this.projects, 'badge')
    }
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
@import '../../../main.scss';


.card {
  font-family: $font-header;
  font-size: 1.5rem;
  justify-content: center;
  word-break: break-word;
  text-align: center;
}

@mixin card_badge {
  position: relative;
  display: inline;
  left: 0.75rem;
  top: 0.75rem;
  padding: 0.3rem 0.75rem;
  border-radius: 25px;
  box-shadow: 2px 3px #2c3e50;
  font-family: $font-content;
  font-size: 1rem;
  font-weight: bold;
}

.card_badge--active {
  background-color: green;
  @include card_badge;

  &::after {
    content: 'Aktywny'
  }
}

.card_badge--maintained {
  background-color: yellow;
  @include card_badge;

  &::after {
    content: 'Wspierany'
  }
}

.card_badge--parked {
  background-color: red;
  @include card_badge;

  &::after {
    content: "zaparkowany"
  }
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
