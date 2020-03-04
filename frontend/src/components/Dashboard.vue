<template>
  <div>
    <app-dashboard-header />
    <app-hacknight />
  </div>
</template>

<script>
import DashboardHeader from './DashboardHeader.vue';
import Hacknight from './Hacknight.vue';

export default {
  components: {
    'app-dashboard-header': DashboardHeader,
    'app-hacknight': Hacknight
  }
};
</script>

<style lang="scss" scoped></style>
