<template>
  <div>
    <footer>Copyright © Code for Poznan {{ currentYear }}</footer>
  </div>
</template>

<style lang="scss" scoped>
@import '../../../main.scss';
footer {
  color: $white;
  background-color: $blue-nav-footer;
  padding: 25px 0;
  display: flex;
  justify-content: center;
}
</style>

<script>
export default {
  data() {
    return {
      currentYear: new Date().getFullYear()
    }
  }
}
</script>
