<template>
    <v-container text-xs-center id="blue-container">
        <v-row>
            <v-col>
                <v-card flat dark tile color="transparent">
                    <v-card-text id="white-title">O NAS</v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row wrap>
            <v-col md6 xs12>
                <v-card flat dark tile color="transparent">
                    <v-card-text>
                        <p id="sub-title">Kim jesteśmy?</p>
                        <p id="content">
                            Grupą osób, która uważa, że warto ulepszać świat za
                            pomocą technologii i chce dostarczać narzędzia,
                            dzięki którym każdy będzie mógł to robić.
                        </p>

                        <p />
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col md6 xs12>
                <v-card flat dark tile color="transparent">
                    <v-card-text wrap id="content">
                        <p id="sub-title">Co robimy?</p>
                        <p id="content">
                            Projektujemy. Programujemy. Testujemy. Poprawiamy.
                            Tworzymy aplikacje społeczne, które aktywują
                            użytkowników do działania na rzecz swojej
                            społeczności czy jakiegoś interesu społecznego.
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
