<template>
  <v-item-group>
    <v-container grid-list>
      <v-layout row wrap>
        <v-flex class="flexPadding" v-for="project in projects" xs12 md6 lg4 xl3>
          <v-hover>
          <v-card slot-scope="{ hover }" :class="onHover()">
            <v-img :src="project.image" aspect-ratio="1.9"></v-img>
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out v-card--reveal display-3"
                  style="height: 100%">Zobacz więcej</div>
              </v-expand-transition>
          </v-card>
          </v-hover>
    </v-flex>
  </v-layout>
</v-container>
  </v-item-group>
</template>

<script>
  export default {
    data () {
      return {
        hovered: false,
        projects: [
          {name: 'Volontulo', image: require('@/assets/volontulo.png')},
          {name: 'Wysadź ulicę', image: require('@/assets/wysadz_ulice.png')},
          {name: 'Bank Empatii', image: require('@/assets/bank_empatii.png')},
          {name: 'Alinka'},
          {name: 'Polska Akcja Humanitarna'}
        ]
      }
    },

    methods: {
      onHover() {

      }
    }
  }
</script>

<style>
  .flexPadding {
    padding: 10px
  }

  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .8;
    position: absolute;
    width: 100%;
    background: red;
    text-decoration-color: yellow;
  }
</style>