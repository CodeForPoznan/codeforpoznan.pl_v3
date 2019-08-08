<template>
    <v-container>
        <v-layout row wrap>
            <v-flex
                id="items"
                v-for="(project, index) in projects"
                :key="index"
                xs12
                md6
                lg4
                xl3
            >
                <v-item-group>
                    <v-hover v-slot="{ hover }">
                        <v-card @click.stop="clickImage(project)">
                            <v-img
                                :src="project.image"
                                aspect-ratio="1.9"
                            ></v-img>
                            <v-card-title>
                                {{ project.name }}
                            </v-card-title>
                            <v-expand-transition>
                                <div v-if="hover" id="card--reveal">
                                    <v-img
                                        id="hoverd-img"
                                        :src="hoveredImg"
                                    ></v-img>
                                </div>
                            </v-expand-transition>
                        </v-card>
                    </v-hover>
                </v-item-group>
            </v-flex>
        </v-layout>
        <v-dialog v-model="dialog" width="300">
            <app-modal-content
                :selectedProject="selectedProject"
                :dialog="dialog"
            ></app-modal-content>
        </v-dialog>
    </v-container>
</template>

<script>
import ModalContent from './OurProjects-ModalContent.vue';
export default {
    components: {
        'app-modal-content': ModalContent
    },
    data() {
        return {
            hoveredImg: require('@/assets/images/Antu_dialog-icon-preview.svg'),
            selectedProject: [],
            dialog: false,
            projects: [
                {
                    name: 'Volontulo',
                    image: require('@/assets/images/volontulo.png'),
                    description: 'cokolwiek'
                },
                {
                    name: 'Wysadź ulicę',
                    image: require('@/assets/images/wysadz_ulice.png')
                },
                {
                    name: 'Bank Empatii',
                    image: require('@/assets/images/bank_empatii.png')
                },
                {
                    name: 'Alinka',
                    image: ''
                },
                {
                    name: 'Polska Akcja Humanitarna',
                    image: ''
                }
            ]
        };
    },
    methods: {
        clickImage(project) {
            this.dialog = true;
            this.selectedProject = project;
        }
    }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

#items {
    padding: 10px;
}

#card--reveal {
    background: $blue;
    bottom: 0;
    color: $white;
    display: flex;
    justify-content: center;
    opacity: 0.9;
    position: absolute;
    width: 100%;
    height: 100%;
}

#hoverd-img {
    max-width: 50%;
}

#modal-content {
    background: $white;
}
</style>
