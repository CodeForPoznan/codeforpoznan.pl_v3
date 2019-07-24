<template>
    <v-item-group>
        <v-container grid-list>
            <v-layout wrap>
                <v-flex
                    id="items"
                    v-for="project in projects"
                    :key="project.name"
                    xs12
                    md6
                    lg4
                    xl3
                >
                    <v-hover>
                        <v-card slot-scope="{ hover }" @click.stop="clickImage">
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
                            <v-dialog v-model="dialog" width="300">
                                <v-card>
                                    <v-card-title>
                                        {{ project.name }}
                                    </v-card-title>
<!--                                    <v-card-actions>-->
<!--                                        <v-btn @click="clickImage">-->
<!--                                        zamknij-->
<!--                                        </v-btn>-->
<!--                                    </v-card-actions>-->
                                </v-card>
                            </v-dialog>
                        </v-card>
                    </v-hover>
                </v-flex>
            </v-layout>
        </v-container>
    </v-item-group>
</template>

<script>
export default {
    data() {
        return {
            hoveredImg: require('@/assets/images/Antu_dialog-icon-preview.svg'),
            dialog: false,
            projects: [
                {
                    name: 'Volontulo',
                    image: require('@/assets/images/volontulo.png'),
                    description: 'cokolwiek'
                },
                {
                    name: 'Wysadź ulicę',
                    image: require('@/assets/images/wysadz_ulice.png'),
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
    methods:{
        clickImage() {
            this.dialog = !this.dialog;
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
