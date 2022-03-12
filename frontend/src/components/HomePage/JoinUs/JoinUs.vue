<template>
  <v-container fluid class="blue-container" id="join">
    <v-row>
      <v-col>
        <v-card flat dark tile color="transparent">
          <v-card-text class="title">
            <p class="white-title">DOŁĄCZ DO NAS</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row d-flex justify-center>
      <v-col>
        <v-card flat dark tile color="transparent">
          <p class="content">
            Kodujesz? Testujesz? Zajmujesz się grafiką albo UX-em? A może
            sprawnie zarządzasz projektami IT?
          </p>
          <br />
          <p class="content">
            W czasie pandemii spotykamy się zdalnie, co tydzień w środę o 18:00.
            Jednak mamy nadzieję, że niedługo wrócimy do stacjonarnych spotkań w
            dobrym towarzystwie.
          </p>
          <br />
          <p class="content">
            Dołącz do nas! Napisz albo zapisz się na wydarzenie onboardingowe.
          </p>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style lang="scss" scoped>
@import '../../../main.scss';

.content {
  margin: auto;
  max-width: 60%;
}
</style>
