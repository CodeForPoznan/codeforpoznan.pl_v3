<template id="modal">
    <v-card>
        <v-layout row wrap>
            <v-card-title id="title">
                {{ selectedProject.name }}
            </v-card-title>
            <v-card-actions></v-card-actions>
            <v-btn flat round :href="selectedProject.website" target="_blank">
                <v-icon>language</v-icon> Strona
            </v-btn>
            <v-btn flat round :href="selectedProject.github" target="_blank">
                <v-icon>fab fa-github</v-icon> Repozytorium
            </v-btn>
            <v-btn icon @click="onClick()">
                <v-icon>close</v-icon>
            </v-btn>
        </v-layout>
        <v-card-text id="content">
            <v-layout>
                Licencja:
                <v-btn
                    round
                    flat
                    :href="selectedProject.licensePage"
                    target="_blank"
                >
                    {{ selectedProject.license }}
                </v-btn>
            </v-layout>
            <v-layout>
                Partner projektu:
                <v-btn
                    round
                    flat
                    :href="selectedProject.partnerPage"
                    target="_blank"
                >
                    {{ selectedProject.partner }}
                </v-btn>
            </v-layout>
            <v-layout>
                {{ selectedProject.description }}
            </v-layout>
            <v-layout>
                Stack:
                <v-btn
                    v-for="(item, index) in selectedProject.stack"
                    :key="index"
                    :href="item.documentation"
                    target="_blank"
                    round
                >
                    {{ item.type }}: {{ item.name }} {{ item.version }}
                </v-btn>
            </v-layout>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    props: ['selectedProject', 'dialog'],
    methods: {
        onClick() {
            this.$root.$emit('close');
        }
    }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

#title {
    font-family: $font-header;
    font-size: 3rem;
    position: relative;
}

#content {
    font-family: $font-content;
    font-size: 1.5rem;
    margin: 0px 0px 10px;
    line-height: 1.43;
}
</style>
