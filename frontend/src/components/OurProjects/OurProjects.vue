<template src="./OurProjects.html"/>

<script>
  export default {
    data () {
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
            image: '',
          },
          {
            name: 'Polska Akcja Humanitarna',
            image: '',
          },
        ]
      }
    },
  }
</script>

<style lang="scss" scoped>
@import "./OurProjects";
</style>
