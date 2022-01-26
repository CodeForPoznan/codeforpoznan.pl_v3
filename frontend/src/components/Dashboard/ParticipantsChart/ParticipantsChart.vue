<template>
  <div class="participants-chart-container">
    <h2 data-test-id="chart-title">Participants on hacknights</h2>
    <div class="range-container">
      <div class="range">
        <div class="start-date">
          <label for="start-date">Start date:</label>
          <input
            type="date"
            id="start-date"
            name="start-date"
            v-model="startDate"
            class="range-input"
          />
        </div>
        <div class="end-date">
          <label for="end-date">End date:</label>
          <input
            type="date"
            id="end-date"
            name="end-date"
            v-model="endDate"
            class="range-input"
          />
        </div>
      </div>
    </div>
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
import { getDateString, getYearBeforeDate } from '../../../helpers/date';

export default {
  data() {
    return {
      todayDate: new Date(),
      startDate: null,
      endDate: null
    };
  },
  mounted() {
    this.startDate = getDateString(getYearBeforeDate(this.todayDate));
    this.endDate = getDateString(this.todayDate);
  },
  computed: {
    ...mapGetters('hacknight', ['getHacknights']),
    hacknightsToDisplay() {
      return this.getHacknights
        .filter(({ date }) => {
          return date > this.startDate && date < this.endDate;
        })
        .reverse();
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
  text-align: center;
}
.range-container {
  display: flex;
  margin: 25px 0;
  flex-direction: column;
  align-items: center;
}
.range {
  display: flex;
  margin-top: 10px;
  align-items: baseline;
  color: #6e8192;
}
.range-input {
  border: 1px solid black;
  color: #6e8192;
  border-radius: 5px;
  margin-right: 5px;
  padding: 4px 10px;
}
.start-date,
.end-date {
  display: flex;
  flex-direction: column;
}
.end-date {
  margin-left: 20px;
}
</style>
