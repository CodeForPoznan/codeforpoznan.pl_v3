<template src="./OurProjects.html"/>

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

    methods: {
      onHover() {

      }
    }
  }
</script>
