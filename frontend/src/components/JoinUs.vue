<template>
  <div id="container">
    <v-container fluid text-xs-center>
      <v-layout row id="white-title">
        <v-flex>
          <v-card flat dark tile color="transparent">
            <v-card-text>DOŁĄCZ DO NAS</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
      <v-layout row wrap id="content">
        <v-flex md6 xs12>
          <v-card flat dark tile color="transparent">
            <v-card-text>
              Kodujesz? Jesteś grafikiem? UX-owcem? Robisz cokolwiek innego, co
              może się przydać w kodowaniu dla Poznania? Dołącz do nas!
              Spotykamy się w każdą środę od godz. 17:00 w firmie STX Next przy
              ul. Morawskiego 12 (koło Areny).
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<style lang="scss" scoped>
@import './../main.scss';
#container {
  background: $blue;
}

#content {
  font-family: $font-content;
  font-size: 20px;
  margin: 0px 0px 10px;
  line-height: 1.43;
  padding-right: 50px;
  padding-left: 50px;
  justify-content: center;
}
</style>
