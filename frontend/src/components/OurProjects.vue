<template>
    <v-container class="white">
        <v-layout row id="black-title">
            <v-flex>
                <v-card flat color="transparent">
                    <v-card-text>NASZE PROJEKTY</v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
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
                            <v-card-title id="card">
                                {{ project.name }}
                            </v-card-title>
                            <v-expand-transition>
                                <div v-if="hover" id="card--reveal">
                                    <v-img
                                        id="card--hover"
                                        :src="hoveredImg"
                                    ></v-img>
                                </div>
                            </v-expand-transition>
                        </v-card>
                    </v-hover>
                </v-item-group>
            </v-flex>
        </v-layout>
        <v-dialog v-model="dialog" width="50rem">
            <app-modal-content
                :selectedProject="selectedProject"
            ></app-modal-content>
        </v-dialog>
    </v-container>
</template>

<script>
import ModalContent from './ModalContent.vue';
import projects_db from '../assets/projects';
export default {
    components: {
        'app-modal-content': ModalContent
    },
    data() {
        return {
            dialog: false,
            hoveredImg: require('@/assets/images/magnifier.svg'),
            projects: projects_db,
            // projects: [
            //     {
            //         description: '',
            //         github: '',
            //         image: '',
            //         license: '',
            //         licensePage: '',
            //         name: 'Fleet manager',
            //         partner: 'Polska Akcja Humanitarna',
            //         partnerPage: 'https://www.pah.org.pl/',
            //         stack: [
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             },
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             }
            //         ],
            //         website: ''
            //     },
            //     {
            //         description: '',
            //         github: '',
            //         image: '',
            //         license: '',
            //         licensePage: '',
            //         name: 'Alinka',
            //         partner: '',
            //         partnerPage: '',
            //         stack: [
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             },
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             }
            //         ],
            //         website: ''
            //     },
            //     {
            //         description:
            //                 'Portal Volontulo powstał dla ludzi i organizacji skupionych wokół idei pomocy innym poprzez udział we wolontariacie. Celem projektu jest pomoc we wzajemnym odnalezieniu się ludzi, którzy chcą realizować się jako wolontariusze/szki oraz organizacji i instytucji, które takich osób poszukują. Podział na strefę "Wolontariusza" oraz "Strefę organizacji i instytucji" umożliwa użytkownikom zwinną nawigację na stronie.',
            //         github: 'https://github.com/CodeForPoznan/volontulo',
            //         image: require('@/assets/images/volontulo.png'),
            //         license: 'MIT',
            //         licensePage: 'https://pl.wikipedia.org/wiki/Licencja_MIT',
            //         name: 'Volontulo',
            //         partner: 'Wielkopolska Rada Koordynacyjna',
            //         partnerPage: 'https://centrum.wrk.org.pl/',
            //         stack: [
            //             {
            //                 type: 'frontend',
            //                 name: 'Angular',
            //                 version: '2.0',
            //                 documentation: 'https://angular.io/'
            //             },
            //             {
            //                 type: 'backend',
            //                 name: 'Django',
            //                 version: '2.2',
            //                 documentation:
            //                         'https://docs.djangoproject.com/en/2.2/'
            //             }
            //         ],
            //         website: 'http://volontuloapp.org/o'
            //     },
            //     {
            //         description: '',
            //         github: '',
            //         image: require('@/assets/images/bank_empatii.png'),
            //         license: '',
            //         licensePage: '',
            //         name: 'Bank empatii',
            //         partner: '',
            //         partnerPage: '',
            //         stack: [
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             },
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             }
            //         ],
            //         website: ''
            //     },
            //     {
            //         description: '',
            //         github: '',
            //         image: require('@/assets/images/wysadz_ulice.png'),
            //         license: '',
            //         licensePage: '',
            //         name: 'Wysadź ulicę',
            //         partner: '',
            //         partnerPage: '',
            //         stack: [
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             },
            //             {
            //                 type: '',
            //                 name: '',
            //                 version: '',
            //                 documentation: ''
            //             }
            //         ],
            //         website: ''
            //     }
            // ],
            selectedProject: []
        };
    },
    methods: {
        clickImage(project) {
            this.dialog = true;
            this.selectedProject = project;
        }
    },
    mounted() {
        this.$root.$on('close', () => {
            this.dialog = false;
        });
    }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';

#items {
    padding: 10px;
}

#card {
    font-family: $font-header;
    font-size: 1.5rem;
    justify-content: center;
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

#card--hover {
    max-width: 50%;
}
</style>
