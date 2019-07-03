<template>
  <v-app id="nav">
    <v-toolbar flat app class="navbar-custom" color="#2c3e50">
      <v-toolbar-title>
        <a class="text-uppercase white--text" flat href="https://codeforpoznan.pl/">
          <v-img :src="image" alt="logo" width="300px" @mouseover="hover = true" @mouseleave="hover = false" :class="{ active: hover }"></v-img>
        </a>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat color="white" v-for="item in menu" :key="item.icon" :to="item.link" float>{{ item.title }}</v-btn>
      </v-toolbar-items>
      <v-menu class="hidden-md-and-up">
        <v-toolbar-side-icon slot="activator" outline flat color="white"></v-toolbar-side-icon>  
          <v-list>
            <v-list-tile v-for="item in items" :key="item" @click="" onmouseover="this.style.color='#0CAEE7';" onmouseout="this.style.color='';">
              <v-list-tile-title v-text="item"></v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
      </v-menu>
    </v-toolbar>
  </v-app>
</template>

<script>
import logo from '../assets/logo.svg';
export default {
  data () {
    return {
      items: [
            'O nas', 'Nasze projekty', 'Dołącz do nas', 'Kontakt'
          ],
      menu: [
        { title: 'O nas' },
        { title: 'Nasze projekty' },
        { title: 'Dołącz do nas' },
        { title: 'Kontakt' }
      ],
      image: logo,
      hover: false
    }
  },
  
  methods: {
    menuItems () {
      return this.menu
    }
  }

}
</script>

<style scoped lang="css"> 
  @import url('https://fonts.googleapis.com/css?family=Montserrat:400,700,800');
  .navbar-custom {
    font-family: 'Montserrat', sans-serif;
    padding: 25px 0;
  }
  a {
    text-decoration: none;
    font-size: 28px;
    font-weight: 700;
  }
  .active {
    opacity: .8;
  }
  .v-btn {
    font-weight: 700;
  }
  .v-menu {
    margin-right: 20px;
  }
</style>