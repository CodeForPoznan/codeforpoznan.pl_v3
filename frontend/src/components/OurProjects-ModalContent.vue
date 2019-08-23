<template id="modal">
    <v-card>
        <v-layout id="header" row wrap>
            <v-flex>
                <v-card-title id="title">
                    {{ selectedProject.name }}
                </v-card-title>
            </v-flex>
            <v-flex id="close">
                <v-card-actions>
                    <v-btn icon @click="onClick()">
                        <v-icon id="close">close</v-icon>
                    </v-btn>
                </v-card-actions>
            </v-flex>
        </v-layout>
        <v-layout>
            <v-btn
                flat
                round
                :href="selectedProject.licensePage"
                target="_blank"
            >
                <v-icon>far fa-copyright</v-icon>
            </v-btn>
            <v-btn flat round :href="selectedProject.website" target="_blank">
                <v-icon>language</v-icon> Strona
            </v-btn>
            <v-btn flat round :href="selectedProject.github" target="_blank">
                <v-icon>fab fa-github</v-icon> Repozytorium
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
    data() {
        return {
            copyleftIcon: require('@/assets/images/Copyleft.svg')
        };
    },
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

#close {
    display: flex;
    justify-content: end;
    color: $white;
}

#header {
    background: $blue;
}

#title {
    font-family: $font-header;
    font-size: 3rem;
    color: $white;
    position: relative;
    height: 8rem;
}

#content {
    font-family: $font-content;
    font-size: 1.5rem;
    margin: 0px 0px 10px;
    line-height: 1.43;
}
</style>
