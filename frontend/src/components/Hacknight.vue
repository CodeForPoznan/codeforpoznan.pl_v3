<template>
    <v-container fluid text-xs-center>
        <v-row align="center" justify="center">
            <v-col class="d-flex" cols="12" sm="6">
                <v-select
                    v-model="selectedHacknight"
                    :items="hacknights"
                    item-text="date"
                    item-value="id"
                    label="Select Hacknight"
                    @input="onGetHacknight"
                >
                    <template v-slot:append-outer>
                        <v-btn
                            color="blue-grey"
                            class="ma-2 white--text"
                            @click="onCreateHacknight"
                            style="top: -12px"
                            offset-y
                        >
                            <v-icon left dark>mdi-plus</v-icon>
                            New
                        </v-btn>
                    </template>
                </v-select>
            </v-col>
        </v-row>
        <v-container fluid text-xs-center>
            <v-row align="center" justify="center">
                <v-col class="d-flex" cols="12" sm="6">
                    <v-combobox
                        v-model="selectedParticipants"
                        outlined
                        :items="allParticipants"
                        item-text="email"
                        item-value="email"
                        :search-input.sync="search"
                        hide-selected
                        label="Add participants"
                        multiple
                        persistent-hint
                        small-chips
                        clearable
                        deletable-chips
                        append-outer-icon="mdi-cloud-upload"
                    >
                        <template v-if="noData" v-slot:no-data>
                            <v-list-item>
                                <v-list-item-content>
                                    <v-list-item-title>
                                        Select or create hacknight first. No
                                        results matching "<strong>{{
                                            search
                                        }}</strong
                                        >". Press <kbd>enter</kbd> to create a
                                        new one
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </template>
                        <template v-slot:append-outer>
                            <v-btn
                                color="blue-grey"
                                class="ma-2 white--text"
                                @click="onAddParticipants"
                                style="top: -12px"
                                offset-y
                            >
                                <v-icon dark>mdi-cloud-upload</v-icon>
                            </v-btn>
                        </template>
                    </v-combobox>
                </v-col>
            </v-row>
        </v-container>
        <v-card class="mx-auto" color="white" max-width="500">
            <v-toolbar flat color="transparent">
                <v-avatar color="blue" size="48" style="margin-right:1em;">
                    <span class="white--text headline">{{
                        participants.length
                    }}</span>
                </v-avatar>
                <v-toolbar-title>Participants</v-toolbar-title>
                <div class="flex-grow-1"></div>
            </v-toolbar>
            <v-divider v-if="participants"></v-divider>

            <v-list>
                <template v-for="(item, i) in participants">
                    <v-list-item v-if="participants" :key="i">
                        <v-list-item-avatar>
                            <v-icon>mdi-account-outline</v-icon>
                        </v-list-item-avatar>
                        <v-list-item-title
                            v-text="item.email"
                        ></v-list-item-title>
                    </v-list-item>
                </template>
            </v-list>
            <v-divider></v-divider>
        </v-card>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            selectedHacknight: '',
            selectedParticipants: [],
            allParticipants: [],
            hacknight: {},
            hacknights: [],
            participants: [],
            search: null,
            noData: true
        };
    },
    created() {
        this.$store.dispatch('hacknight/getHacknights').then(res => {
            this.hacknights = res.data.hacknights;
        });
    },
    methods: {
        onCreateHacknight() {
            this.$store.dispatch('hacknight/createHacknight').then(res => {
                this.participants = [];
                this.hacknight = res.data.hacknight;
                this.hacknights.push(this.hacknight);
                this.selectedHacknight = this.hacknight.id;
                this.onGetParticipants();
            });
        },
        onGetHacknight() {
            this.$store
                .dispatch('hacknight/getHacknight', this.selectedHacknight)
                .then(res => {
                    this.hacknight = res.data;
                    this.participants = res.data.participants;
                    this.onGetParticipants();
                });
        },
        onGetParticipants() {
            this.$store.dispatch('hacknight/getParticipants').then(res => {
                this.allParticipants = res.data.participants;
                if (this.participants) {
                    this.allParticipants = this.allParticipants.filter(
                        x =>
                            !this.participants.filter(y => y.id === x.id).length
                    );
                }
            });
        },
        onAddParticipants() {
            const ids = [];

            for (const participant of this.selectedParticipants) {
                ids.push(participant.id);
            }
            const params = {
                hacknight_id: this.selectedHacknight,
                participants_ids: ids
            };

            this.$store
                .dispatch('hacknight/addParticipants', params)
                .then(res => {
                    this.participants = res.data.hacknight.participants;
                    this.selectedParticipants = [];
                });
        }
    }
};
</script>

<style lang="scss" scoped>
@import './../main.scss';
</style>
