<template>
  <div class="participants-chart-container">
    <h2 class="d-flex justify-center">Participants on hacknights</h2>
    <apexchart
      width="500"
      type="line"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters('hacknight', ['getHacknights']),
    hacknightsToDisplay() {
      return this.getHacknights.slice(0, 6).reverse();
    },
    chartCategories() {
      return this.hacknightsToDisplay.map(hacknight => hacknight.date);
    },
    chartData() {
      return this.hacknightsToDisplay.map(
        hacknight => hacknight.participants.length
      );
    },
    chartOptions() {
      return {
        chart: { zoom: { enabled: false } },
        stroke: {
          curve: 'smooth'
        },
        xaxis: {
          categories: this.chartCategories
        },
        stacked: false
      };
    },
    series() {
      return [
        {
          name: 'Participants',
          data: this.chartData
        }
      ];
    }
  }
};
</script>

<style>
.participants-chart-container {
  margin: 60px;
}
</style>
