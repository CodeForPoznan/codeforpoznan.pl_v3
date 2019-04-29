<template>
<v-container fluid id="logo-page">
    <v-layout>
            <v-img
                :src="image"
                >
            </v-img>
    </v-layout>
</v-container>
</template>

<script>
export default{
    data () {
        return {
            image: require('@/assets/images/logo_codeforpoznan.svg'),
        }
    }
}
</script>

<style>
    #logo-page {
        background: #07a3e5;
    }
</style>