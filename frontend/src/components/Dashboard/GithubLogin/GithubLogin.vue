<template>
  <div v-html="legacySystemHTML">
  </div>
</template>

<script>
export default {
  data() {
    return {
      // Just like JSX! Oh wait...
      legacySystemHTML: `
        WUUUUT
      `
    }
  }
}
</script>