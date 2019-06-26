<template>
    <div id="container">
        <v-container fluid text-xs-center>
            <v-layout row id="title">
                <v-flex>
                    <v-card flat dark tile color="transparent">
                        <v-card-text>O NAS</v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout row wrap id="content">
                <v-flex md6 xs12>
                    <v-card flat dark tile color="transparent">
                        <v-card-text>
                            KIM JESTEŚMY?
                            <br /><br />
                            Grupą osób, która uważa, że warto ulepszać świat za
                            pomocą technologii i&nbsp;chce dostarczać narzędzia,
                            dzięki którym każdy będzie mógł to robić.
                        </v-card-text>
                    </v-card>
                </v-flex>
                <v-flex md6 xs12>
                    <v-card flat dark tile color="transparent">
                        <v-card-text>
                            CO ROBIMY?
                            <br /><br />
                            Projektujemy. Programujemy. Testujemy. Poprawiamy.
                            Tworzymy aplikacje społeczne, które aktywują
                            użytkowników do działania na rzecz swojej
                            społeczności czy jakiegoś interesu społecznego.
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
#title {
    font-family: $font-header;
    font-size: 42px;
    position: relative;
    padding-bottom: 20px;
}
#title::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 250px;
    height: 5px;
    background-color: $white;
    margin-left: -125px;
}
#content {
    font-family: $font-content;
    font-size: 20px;
    margin: 0px 0px 10px;
    line-height: 1.43;
    padding-right: 50px;
    padding-left: 50px;
}
</style>
