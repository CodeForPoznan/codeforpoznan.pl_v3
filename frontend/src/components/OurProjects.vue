<template>
  <div>
    <v-item-group>
      <v-container grid-list>
        <v-layout row wrap>
          <v-flex class="flexPadding" v-for="project in projects" xs12 md6 lg4 xl3>
            <v-hover>
              <v-card slot-scope="{ hover }">
                <v-img :src="project.image" aspect-ratio="1.9"></v-img>
                <v-expand-transition>
                  <div v-if="hover" class="v-card--reveal" style="height: 100%">
                    <v-img :src="hoveredImg" max-width="50%"></v-img>
                  </div>
                </v-expand-transition>
              </v-card>
            </v-hover>
          </v-flex>
        </v-layout>
      </v-container>
    </v-item-group>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        hoveredImg: require('@/assets/Antu_dialog-icon-preview.svg'),
        projects: [
          {name: 'Volontulo', image: require('@/assets/volontulo.png')},
          {name: 'Wysadź ulicę', image: require('@/assets/wysadz_ulice.png')},
          {name: 'Bank Empatii', image: require('@/assets/bank_empatii.png')},
          {name: 'Alinka'},
          {name: 'Polska Akcja Humanitarna'}
        ]
      }
    },
  }
</script>

<style>
  .flexPadding {
    padding: 10px
  }

  .v-card--reveal {
    display: flex;
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .9;
    position: absolute;
    width: 100%;
    background: #0CAEE7;
    color: white;
  }
</style>