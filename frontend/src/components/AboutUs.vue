<template>
  <v-container fluid class="blue-container" id="about">
    <v-row>
      <v-col>
        <v-card flat dark tile color="transparent">
          <v-card-text class="title">
            <p class="white-title">O NAS</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xl="6" lg="6" md="6" sm="12" xs="12">
        <v-card flat dark tile color="transparent">
          <v-card-text>
            <p class="sub-title">Kim jesteśmy?</p>
            <p class="content">
              Grupą osób, która uważa, że warto ulepszać świat za pomocą
              technologii i chce dostarczać narzędzia, dzięki którym każdy
              będzie mógł to robić.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col xl="6" lg="6" md="6" sm="12" xs="12">
        <v-card flat dark tile color="transparent">
          <v-card-text>
            <p class="sub-title">Co robimy?</p>
            <p class="content">
              Projektujemy. Programujemy. Testujemy. Poprawiamy. Tworzymy
              aplikacje społeczne, które aktywują użytkowników do działania na
              rzecz swojej społeczności czy jakiegoś interesu społecznego.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style lang="scss" scoped>
@import './../main.scss';
</style>
