<template>
    <v-card>
        <v-card-title> {{ selectedProject.name }} </v-card-title>
        <v-card-text> {{ selectedProject.description }}</v-card-text>
        <v-card-actions>
            <v-btn text>Zamknij</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    props: ['selectedProject', 'dialog']
};
</script>

<style lang="scss" scoped>
@import './../main.scss';
</style>
