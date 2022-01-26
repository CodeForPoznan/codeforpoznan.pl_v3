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
              Jesteśmy grupą wolontariuszy. Staramy się pomóc, tworząc
              oprogramowanie dla organizacji społecznych. W Code for Poznań
              działają osoby, które zajmują się pisaniem kodu, zarządzaniem
              projektami, projektowaniem (UX) i testowaniem rozwiązań
              technologicznych. Jesteśmy zróżnicowani i otwarci. Łączy nas jeden
              cel - pomoc organizacjom społecznym.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col xl="6" lg="6" md="6" sm="12" xs="12">
        <v-card flat dark tile color="transparent">
          <v-card-text>
            <p class="sub-title">Co robimy?</p>
            <p class="content">
              Gdy nawiązujemy współpracę z organizacją, staramy się poznać jej
              problemy i przełożyć je na praktyczne rozwiązania technologiczne.
              Szukamy wyzwań, żeby tworzyć oryginalne aplikacje, platformy i
              systemy informatyczne. Nasze projekty ułatwiają organizacjom
              społecznym tworzenie dobra dla innych i angażują użytkowników do
              działania na rzecz ważnych spraw.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style lang="scss" scoped>
@import '../../../main.scss';
</style>
