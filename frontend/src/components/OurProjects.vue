<template>
  <v-container>
    <v-layout row wrap>
      <v-flex
        id="items"
        v-for="project in projects"
        :key="project.name"
        xs12
        md6
        lg4
        xl3
      >
        <v-item-group>
          <v-hover>
            <v-card slot-scope="{ hover }">
              <v-img :src="project.image" aspect-ratio="1.9"></v-img>
              <v-expand-transition>
                <div v-if="hover" id="card--reveal">
                  <v-img id="hoverd-img" :src="hoveredImg"></v-img>
                </div>
              </v-expand-transition>
            </v-card>
          </v-hover>
        </v-item-group>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      hoveredImg: require('@/assets/images/Antu_dialog-icon-preview.svg'),
      projects: [
        {
          name: 'Volontulo',
          image: require('@/assets/images/volontulo.png')
        },
        {
          name: 'Wysadź ulicę',
          image: require('@/assets/images/wysadz_ulice.png')
        },
        {
          name: 'Bank Empatii',
          image: require('@/assets/images/bank_empatii.png')
        },
        {
          name: 'Alinka',
          image: ''
        },
        {
          name: 'Polska Akcja Humanitarna',
          image: ''
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

#items {
  padding: 10px;
}

#card--reveal {
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

#hoverd-img {
  max-width: 50%;
}
</style>
